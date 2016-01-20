# -*- coding: utf-8 -*-
#
# (C) 2016 Rodrigo Rodrigues da Silva <pitanga@members.fsf.org>
#
# This file is part of Neverworm.
#
# Neverworm is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Neverworm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Neverworm.  If not, see <http://www.gnu.org/licenses/>.


from django.utils.translation import ugettext_lazy as _

from users.models import Cluster, Supplier, Worker
from orders.models import Wishlist

import requests
import logging
logger = logging.getLogger(__name__)

def schedule_polls():
    for c in Cluster.objects.all():
        if c.supplier:
            wl = Wishlist(cluster=c, supplier=c.supplier)
            wl.save()
            wl = Wishlist.objects.get(id=wl.id)
            for v in c.villages.all():
                for w in v.workers.all():
                    send_poll(wl, w)

def send_poll(wishlist, worker):
    wishlist.owner = Worker.objects.get(id=3) # XXX: hardcoded
    wishlist.product = 'Nilwormex' # XXX: hardcoded
    if worker.phone_number:
        message = _('Hey, {first_name}, there is a new wishlist for {product} in your area. '
                    'If you are interested please contact {owner_name} from {owner_village} '
                    'at {owner_phone_number}').format(first_name=worker.first_name,
                                                      product=wishlist.product,
                                                      owner_name=wishlist.owner.public_name,
                                                      owner_phone_number=wishlist.owner.phone_number,
                                                      owner_village=wishlist.owner.village.name)
        send_sms(worker.phone_number, message)

def send_sms(number, message):
    logger.debug(_('[SMS or push to {0}] {1}').format(number, message))
    username = 'itu'
    password = 'iTu$m$aLL'
    params = { 'message'  : message,
               'username' : username,
               'password' : password,
               'number'   : number,
               }
    REQUEST_URL = "https://send.smsall.pk/tpapi_gateway.py/outgoing"
    r = requests.get(REQUEST_URL, params=params, verify=False)
    r.raise_for_status()
