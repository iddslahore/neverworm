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
from django.db.models.signals import post_init
from django.dispatch import receiver

from users.models import Cluster, Supplier, Worker
from orders.models import Wishlist

import requests
import logging
logger = logging.getLogger(__name__)


def wishlist_populate():
    for head in Worker.objects.filter(head=True):
        for p in head.village.cluster.supplier.product_offers.all():
            wl = Wishlist(owner=head, cluster=head.village.cluster, product_offer=p)
            wl.save()
            wl = Wishlist.objects.get(id=wl.id)
            for w in head.contacts.all():
                wishlist_alert_new(wl, w)


def wishlist_alert(wishlist):
    for w in wishlist.owner.contacts.all():
        logger.debug("Alerting {}".format(w))
        wishlist_alert_new(wishlist, w)

# @receiver(post_init, sender=Wishlist)
# def wishlist_create_handler(sender,kwargs):

def wishlist_alert_new(wishlist, worker):
    if worker.phone_number:
        message = _('Hey, {first_name}, there is a new wishlist for {product} in {cluster}. '
                    'If you are interested please contact {owner_name} from {owner_village} '
                    'at {owner_phone_number}').format(first_name=worker.first_name,
                                                      product=wishlist.product.description,
                                                      cluster=wishlist.owner.village.cluster,
                                                      owner_name=wishlist.owner.public_name,
                                                      owner_phone_number=wishlist.owner.phone_number,
                                                      owner_village=wishlist.owner.village.name)
        send_sms(worker.phone_number, message)

def send_sms(number, message):
    logger.debug(_('[SMS or push to {number}] {message}').format(number=number, message=message))
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
