## -*- coding: utf-8 -*- ####################################################

from django.forms.widgets import MediaDefiningClass

class ImageEditToolBasic():
    __metaclass__ = MediaDefiningClass

    name = None

    def render_button(self, attrs, filter_name):
        raise NotImplementedError

    def render_initial(self, attrs, filter_name):
        raise NotImplementedError

    def proceed_image(self, image, params):
        raise NotImplementedError