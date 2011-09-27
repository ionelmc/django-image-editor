## -*- coding: utf-8 -*- ####################################################

from django.forms.widgets import MediaDefiningClass
from django.utils import simplejson

class ImageEditToolBasic(object):
    __metaclass__ = MediaDefiningClass

    def __init__(self, name, options=None):
        self.name = name
        self.options = simplejson.dumps(options or {})

    def render_button(self, attrs, filter_name):
        raise NotImplementedError

    def render_initial(self, attrs, filter_name):
        raise NotImplementedError

    def proceed_image(self, image, params):
        raise NotImplementedError