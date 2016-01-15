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


from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import Cluster, Supplier, Worker

# Create your models here.


class Request(models.Model):
    cluster = models.ForeignKey(Cluster)
    supplier = models.ForeignKey(Supplier)
    submission_date = models.DateTimeField(auto_now_add=True, null=False)
    target_date = models.DateField(null=True, blank=True)


class RequestItem(models.Model):
    request = models.ForeignKey(Request, null=False, blank=False, related_name='items')
    worker = models.ForeignKey(Worker, null=False, blank=False)
    name = models.CharField(_("name"), default = "Nilzan", max_length=20, null=False, blank=False)
    quantity = models.IntegerField(_("quantity"), default = "0", null=False, blank=False)
