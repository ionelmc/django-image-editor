## -*- coding: utf-8 -*- ####################################################
#from simplejson.decoder import JSONDecodeError

from django.core.exceptions import ValidationError
from django.forms.fields import Field
from django.utils import simplejson
from django.utils.simplejson.decoder import JSONDecoder
from django.utils.translation import ugettext


from image_editor.widgets import ImageEditWidget
from image_editor.utils import apply_filters_to_image

class ImageEditFormField(Field):
    widget = ImageEditWidget
    operations = []

    def __init__(self, *args, **kwargs):
        super(ImageEditFormField, self).__init__(*args, **kwargs)

    def apply_to_image(self, image_name):
        return apply_filters_to_image(image_name, self.operations)

    def clean(self, value):
        try:
            data = simplejson.loads(value)
            self.operations = data.get('operations')
            value = self.apply_to_image(data.get('image'))
        except Exception:
            raise ValidationError(ugettext('Image edit data is not valid'))

        return super(ImageEditFormField, self).clean(value)