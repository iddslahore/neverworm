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


# from django.db import models
# from django.utils.translation import ugettext_lazy as _

# from users.models import Farmer, Worker

# # Create your models here.

# class Visit(models.Model):
#     date = models.DateTimeField(_("date of visit"))
#     next_visit = models.DateField(_("next visit"))
#     doses_applied = models.IntegerField(_("doses applied"))
#     mecicine_applied = models.CharField(_("medicine applied"), default = "Nilzan", max_length=20)
#     worker = models.ForeignKey(Worker, related_name='visits')
#     farmer = models.ForeignKey(Farmer, related_name='visits')

#     def is_past():
#         pass

#     def is_due():
#         pass
