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


from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from orders.models import Wishlist, WishlistItem
from users.models import Worker

import logging
logger = logging.getLogger(__name__)


class WishlistView(TemplateView):
    template_name="wishlist.html"


def wishlist_detail(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    worker = Worker.objects.get(id=1) # XXX hardcoded
    return render(request, 'wishlist.html', {
        'worker' : worker,
        'wishlist' : wishlist,})


def place_wish(request, pk):
    worker = Worker.objects.get(id=1) # XXX hardcoded
    try:
        quantity = int(request.POST['quantity'])
        logger.debug(quantity)
    except (KeyError):
        quantity = 0
    active_wishlist = get_object_or_404(Wishlist, pk=pk)
    if not active_wishlist.is_active:
        logger.debug("redirect to dashboard with message 'wishlist not active'")
        error_message = _("Wishlist not active!")
    elif not active_wishlist.can_participate(worker):
        logger.debug("redirect to dashboard with message 'not allowed'")
        error_message = _("Not allowed!")
    elif active_wishlist.is_participant(worker):
        logger.debug("redirect to dashboard with message 'you have already voted'")
        #or update??
        error_message = _("You have already voted!")
    else:
        wish = WishlistItem(worker=worker, quantity=quantity, wishlist=active_wishlist)
        wish.save()
        active_wishlist.amount += wish.quantity
        active_wishlist.save()
        logger.error("redirect to dashboard with message 'you have successfully placed your wish'")
        error_message = _("Thank you!") 
        logger.debug("emit signal wish_placed")


    return HttpResponseRedirect(reverse('wishlist_detail', args=(active_wishlist.id,))) # TODO: put error messages in context

