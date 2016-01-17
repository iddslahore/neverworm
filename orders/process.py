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

from users.models import Cluster, Supplier
from orders.models import Wishlist

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
    if worker.phone_number:
        logger.debug(_('[SMS or push to %(phone_number)s] Hey, %(first_name)s, there is a new poll deadline is %(target_date)s')
                     % {'phone_number': worker.phone_number,
                        'first_name' : worker.first_name,
                        'target_date' : wishlist.target_date,
                    })
