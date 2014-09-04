# -*- coding:utf-8 -*-
# author:sundayliu

from django.conf import settings
from models import Paste

import datetime

today = datetime.datetime.today()
cutoff = today - datetime.timedelta(days=settings.EXPIRY_DAYS)
Paste.objects.filter(timestamp__lt=cutoff).delete()