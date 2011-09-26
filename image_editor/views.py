## -*- coding: utf-8 -*- ####################################################
import os
import datetime

from django.core.files.storage import default_storage as storage # TODO: allow set storage via settings
from django.http import HttpResponse
from django.utils import simplejson

from image_editor.utils import apply_filters_to_image
from image_editor.settings import EDITED_PREVIEWS_ROOT

def make_preview(request):
    result = {'success': False}
    try:
        operations = simplejson.loads(request.POST.get('operations'))
        image_name = request.POST.get('image')
        shortname, extension = os.path.splitext(image_name)

        result_image = storage.save(
            os.path.join(EDITED_PREVIEWS_ROOT, datetime.datetime.now().isoformat() + extension),
            apply_filters_to_image(image_name, operations)
        )

        result['image'] = storage.url(result_image)
        result['success'] = True
    except Exception, e:
        result['error'] = e.message

    return HttpResponse(simplejson.dumps(result), content_type="application/json; charset=utf-8")