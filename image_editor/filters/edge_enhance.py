## -*- coding: utf-8 -*- ####################################################
import ImageFilter

from django.conf import settings
from django.utils.translation import ugettext

from image_editor.filters.basic import ImageEditToolBasic

class ImageEdgeEnhanceFilter(ImageEditToolBasic):

    def render_button(self, attrs, filter_name):
        return '<img src="%(static_url)s%(image_url)s" /><br/>%(filter_title)s\
                <span class="filter_auto_apply" filter_name="%(name)s" filter_params="{}"></span>' % \
        dict(
            static_url=settings.STATIC_URL,
            image_url='image_editor/img/edge_enhance.jpeg',
            name=filter_name,
            filter_title=ugettext('Edge enhance')
        )

    def render_initial(self, attrs, filter_name):
        return ""

    def proceed_image(self, image, params):
        return image.filter(ImageFilter.EDGE_ENHANCE)