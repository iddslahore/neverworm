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
from django.views.generic import ListView, CreateView
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from orders.models import Wishlist, WishlistItem, ProductOffer
from users.models import Worker
from orders import process

import logging
logger = logging.getLogger(__name__)


class Dashboard(ListView):
    model = Wishlist
    template_name = 'dashboard.html'

    def get_queryset(self):
        worker = get_object_or_404(Worker, user_id=self.request.user.id)
        return Wishlist.objects.filter(cluster=worker.village.cluster)[0:5]

@login_required
def wishlist_create(request):
    worker = get_object_or_404(Worker, user_id=request.user.id)

    if request.method == 'GET':
        product_offers = ProductOffer.objects.filter(supplier__cluster=worker.village.cluster)

        return render(request, 'wishlist_create.html', {
            'worker' : worker,
            'product_offers' : product_offers})

    elif request.method == 'POST':
        try:
            product_offer_id = request.POST['p']
            logger.debug("product_offer_id: {}".format(product_offer_id))
        except (KeyError):
            error_message = _("Error. Invalid product!")
            logger.debug("Error. Invalid product!")
            # error message
            pass
        worker = get_object_or_404(Worker, user_id=request.user.id)
        product_offer = get_object_or_404(ProductOffer, id=product_offer_id)
        wishlist = Wishlist.objects.create(owner = worker,
                                           cluster = worker.village.cluster,
                                           product_offer = product_offer,
                                           status = 'P')
        wishlist = Wishlist.objects.get(id=wishlist.id)
        error_message = _("You have successfully created your wishlist! Thank you!")
        logger.debug("TODO: emit signal wishlist_created")
        #TODO: conectar com signal
        process.wishlist_alert(wishlist)

    return render(request, 'dashboard.html', {
        'error_message' : error_message,})


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
