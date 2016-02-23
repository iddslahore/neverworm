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


from __future__ import absolute_import
from celery import shared_task

import requests

import logging
logger = logging.getLogger(__name__)


@shared_task
def send_sms(number, message):
    logger.debug(('[Sending SMS to {number}] {message}').format(number=number, message=message))
    username = 'itu'
    password = 'iTu$m$aLL'
    params = { 'message'  : message,
               'username' : username,
               'password' : password,
               'number'   : number,
               }
    #REQUEST_URL = "https://send.smsall.pk/tpapi_gateway.py/outgoing"
    REQUEST_URL = "http://127.0.0.1:8080"
    r = requests.get(REQUEST_URL, params=params, verify=False)
    r.raise_for_status()
