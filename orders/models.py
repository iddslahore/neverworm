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


class Product(models.Model):
    description = models.CharField(_("description"), default = "Nilzan Plus 1000 ml", max_length=20, null=False, blank=False)
    manufacturer = models.CharField(_("manufacturer"), default = "ICI", max_length=20, null=False, blank=False)


class ProductOffer(models.Model):
    product = models.ForeignKey(Product)
    supplier = models.ForeignKey(Supplier)
    min_order = models.IntegerField(_("minimum order"), null=False, blank=False, default=0)
    unit_price = models.DecimalField(_("unit price"), decimal_places=2, max_digits=10, null=False, blank=False, default=0)


class Wishlist(models.Model):

    STATUS_CHOICES = (
        ('N', _('NEW')),
        ('P', _('PUBLISHED')),
        ('Q', _('QUOTED')),
        ('S', _('SHIPPED')),
        ('C', _('CANCELLED')),
    )

    owner = models.ForeignKey(Worker)
    product = models.ForeignKey(Product)
    cluster = models.ForeignKey(Cluster)
    supplier = models.ForeignKey(Supplier)
    submission_date = models.DateTimeField(_("submission date"), auto_now_add=True, null=False)
    shipping_date = models.DateTimeField(_("shipping date"), null=False, blank=False)
    amount = models.IntegerField(_("amount"), default=0, null=False, blank=False)
    status = models.CharField(_("status"), max_length=1, default='N', choices=STATUS_CHOICES)

    def __str__(self):
        return _("{goal} units of {product} in {cluster}").format(goal=self.goal,
                                                                  product=self.product,
                                                                  cluster=self.cluster)

    @property
    def is_new(self):
        return self.status == 'N'

    @property
    def is_published(self):
        return self.status == 'P'

    @property
    def is_quoted(self):
        return self.status == 'Q'

    @property
    def is_shipped(self):
        return self.status == 'S'

    @property
    def is_canceled(self):
        return self.status == 'C'

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

    def is_participant(self, worker):
        return self.items.filter(worker=worker).count()

    def can_participate(self, worker):
        return worker.village in self.cluster.villages.all()


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, related_name='items')
    worker = models.ForeignKey(Worker, null=False, blank=False)
    quantity = models.IntegerField(_("quantity"), default = 0, null=False, blank=False)

    def __str__(self):
        return _("{quantity} units for {name}").format(quantity=self.quantity,
                                                       name=self.worker)
