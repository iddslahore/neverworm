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
from django.core.validators import RegexValidator
from django.contrib.auth.models import User as DjangoUser

import logging
logger = logging.getLogger(__name__)


# Create your models here.

class Cluster(models.Model):
    supplier = models.ForeignKey('Supplier', related_name='cluster', null=True, blank=True)
    name = models.CharField(_("name"), max_length = 50, blank=False)

    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(_("name"), max_length = 50, blank=False)
    cluster = models.ForeignKey(Cluster, null=False, blank=False, related_name='villages')

    def __str__(self):
        return self.name + ', ' + self.cluster.name


class User(DjangoUser):

    class Meta:
        proxy = True


class Person(models.Model):
    
    GENDER_CHOICES = (
            ('M', _('Male')),
            ('F', _('Female')),
            ('U', _('Undefined')),
        
        )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=_("Phone number must be entered in the format: \
                                 '+999999999'. Up to 15 digits allowed."))

    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(_("first name"), max_length=128, null=False, blank=False)
    last_name = models.CharField(_("last name"), max_length=128, blank=True)
    latitude = models.CharField(_("latitude"), max_length=128, blank=True)
    longitude = models.CharField(_("longitude"), max_length=128, blank=True)
    phone_number = models.CharField(_("phone number"), validators=[phone_regex], max_length=16, blank=True)
    gender = models.CharField(_("gender"), max_length=1, choices=GENDER_CHOICES, default='U')

    class Meta:
        abstract = True

    def __str__(self):
        return self.public_name

    @property
    def public_name(self):
        return (
            self.first_name +
            ' ' +
            self.last_name[
                0:1] +
            '.') if self.first_name and self.last_name else self.user.username


class Farmer(Person):
    animal_count = models.IntegerField(_("animal count"))


class Worker(Person):
    village = models.ForeignKey(Village, null=False, blank=False, related_name='workers')
    training_completion = models.DateField(_("training completion"))
    stock = models.IntegerField(_("stock"), default=0, null=False)


class Supplier(Person):
    snail_mail = models.CharField(_("address"), max_length = 1000, blank="True")
    minimum_order = models.IntegerField(_("minimum order"), null=False, blank=False, default=0)

    def __str__(self):
        return self.first_name
