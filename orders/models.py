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

import datetime

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from users.models import Cluster, Supplier, Worker

# Create your models here.

def default_target_date():
    delta_days = settings.DEADLINE_DELTA_DAYS
    return timezone.now() + datetime.timedelta(days=delta_days)


class Wishlist(models.Model):
    product = models.CharField(_("product"), default = "Nilzan 500ml", max_length=20, null=False, blank=False)
    cluster = models.ForeignKey(Cluster)
    supplier = models.ForeignKey(Supplier)
    submission_date = models.DateTimeField(_("submission date"), auto_now_add=True, null=False)
    target_date = models.DateTimeField(_("target date"), default=default_target_date, null=False, blank=False)
    amount = models.IntegerField(_("amount"), default=0, null=False, blank=False)

    @property
    def goal(self):
        return self.supplier.minimum_order

    @property
    def progress(self):
        if self.goal < 1:
            return 0
        else:
            return self.amount / self.goal

    @property
    def is_expired(self):
        return timezone.now() > self.target_date

    @property
    def is_success(self):
        return self.amount >= self.goal

    @property
    def is_active(self):
        return not self.is_expired

    def is_participant(self, worker):
        return self.items.filter(worker=worker).count()

    def can_participate(self, worker):
        return worker.village in self.cluster.villages.all()


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, related_name='items')
    worker = models.ForeignKey(Worker, null=False, blank=False)
    quantity = models.IntegerField(_("quantity"), default = "0", null=False, blank=False)
