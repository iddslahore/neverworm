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
from django.utils.translation import ugettext_lazy as _

from orders.models import Wishlist, WishlistItem, Product, ProductOffer


class WishlistItemAdmin(admin.ModelAdmin):
    model = WishlistItem


class WishlistItemInline(admin.TabularInline):
    model = WishlistItem
    extra = 0
    verbose_name_plural = _("items")

    
class WishlistAdmin(admin.ModelAdmin):
    model = Wishlist
    inlines = (WishlistItemInline,)


class ProductOfferInline(admin.TabularInline):
    model = ProductOffer
    extra = 0
    verbose_name_plural = _("product offers")


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = (ProductOfferInline,)


admin.site.register(WishlistItem, WishlistItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Wishlist, WishlistAdmin)
