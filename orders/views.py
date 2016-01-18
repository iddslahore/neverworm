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
from django.views.generic import ListView
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from orders.models import Wishlist, WishlistItem
from users.models import Worker

import logging
logger = logging.getLogger(__name__)


@login_required
class Dashboard(ListView):
    model = Wishlist
    template_name = 'dashboard.html'

    def get_queryset(self):
        worker = get_object_or_404(Worker, user_id=self.request.user.id)
        return Wishlist.objects.filter(cluster=worker.village.cluster)


@login_required
def wishlist_detail(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    worker = get_object_or_404(Worker, user_id=request.user.id)
    return render(request, 'wishlist.html', {
        'worker' : worker,
        'wishlist' : wishlist,})


@login_required
def place_wish(request, pk):
    worker = get_object_or_404(Worker, user=request.user)
    try:
        quantity = int(request.POST['quantity'])
    except (KeyError):
        quantity = 0

    active_wishlist = get_object_or_404(Wishlist, pk=pk)
    if not active_wishlist.is_active:
        error_message = _("Wishlist not active!")
    elif not active_wishlist.can_participate(worker):
        error_message = _("You are not allowed to join a wishlist that is not in your area!")
    elif active_wishlist.is_participant(worker):
        error_message = _("You have already joined this wishlist!")
    else:
        wish = WishlistItem(worker=worker, quantity=quantity, wishlist=active_wishlist)
        wish.save()
        active_wishlist.amount += wish.quantity
        active_wishlist.save()
        error_message = _("You have successfully placed your order! We will let you know when the deal is closed. Thank you!")
        logger.debug("TODO: emit signal wish_placed")

    return render(request, 'dashboard.html', {
        'error_message' : error_message,})
