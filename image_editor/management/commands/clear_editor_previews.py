### -*- coding: utf-8 -*- ####################################################
import datetime

from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

from image_editor.settings import EDITED_PREVIEWS_ROOT

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        time = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        for file in default_storage.listdir(EDITED_PREVIEWS_ROOT)[1]:
            if default_storage.created_time('%s/%s' % (EDITED_PREVIEWS_ROOT, file)) + delta < time:
                default_storage.delete('%s/%s' % (EDITED_PREVIEWS_ROOT, file))