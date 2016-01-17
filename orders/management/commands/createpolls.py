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


from django.core.management.base import BaseCommand, CommandError

from orders import process
from orders.process import schedule_polls

import logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Create polls for group buy'

    def handle(self, *args, **options):
        process.schedule_polls()
        self.stdout.write(self.style.SUCCESS('Successfully created polls'))
