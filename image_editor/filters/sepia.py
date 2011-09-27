## -*- coding: utf-8 -*- ####################################################
import ImageOps

from django.conf import settings
from django.utils.translation import ugettext

from image_editor.filters.basic import ImageEditToolBasic

class ImageSepiaFilter(ImageEditToolBasic):

    def render_button(self, attrs, filter_name):
        return '<img src="%(static_url)s%(image_url)s" /><br/>%(filter_title)s\
                <span class="filter_auto_apply" filter_name="%(name)s" filter_params="{}"></span>' % \
        dict(
            static_url=settings.STATIC_URL or settings.MEDIA_URL,
            image_url='image_editor/img/sepia.jpeg',
            name=filter_name,
            filter_title=ugettext('Sepia')
        )

    def render_initial(self, attrs, filter_name):
        return ""

    def make_linear_ramp(self, white):
        # putpalette expects [r,g,b,r,g,b,...]
        ramp = []
        r, g, b = white
        for i in range(255):
            ramp.extend((r*i/255, g*i/255, b*i/255))
        return ramp

    def proceed_image(self, image, params):
        if image.mode != "L":
            image = image.convert("L")

        # optional: apply contrast enhancement here, e.g.
        image = ImageOps.autocontrast(image)

        sepia = self.make_linear_ramp((255, 240, 192))
        
        # apply sepia palette
        image.putpalette(sepia)

        # convert back to RGB so we can save it as JPEG
        # (alternatively, save it in PNG or similar)
        return image.convert("RGB")