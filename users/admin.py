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


from django.contrib import admin
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.admin import UserAdmin

from users.models import User, Person, Worker, Supplier, Cluster, Village


class UserAdmin(UserAdmin):
    model = User

class PersonAdmin(admin.ModelAdmin):
    model = Person

class WorkerAdmin(PersonAdmin):
    model = Worker

class SupplierAdmin(PersonAdmin):
    model = Supplier

class VillageAdmin(admin.ModelAdmin):
    model = Village

class ClusterAdmin(admin.ModelAdmin):
    model = Cluster


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(Cluster, ClusterAdmin)

admin.site.unregister(DjangoUser) #original User
admin.site.register(User, UserAdmin)
