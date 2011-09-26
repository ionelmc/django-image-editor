## -*- coding: utf-8 -*- ####################################################
from django.conf import settings
from django.utils.translation import ugettext

from image_editor.filters.basic import ImageEditToolBasic

class ImageCropTool(ImageEditToolBasic):

    class Media:
        js = ('jcrop/js/jquery.Jcrop.min.js', 'jcrop/js/cropper.js')
        css = { 'all': ('jcrop/css/jquery.Jcrop.css', ) }

    def render_button(self, attrs, filter_name):
        return '<img src="%(static_url)s%(image_url)s" style="margin: 6px;" /><br/>%(filter_title)s \
                <script>$(function(){ $("#%(id)s_button_crop").cropper("%(id)s") });</script>' % \
               dict(
                    static_url=settings.STATIC_URL,
                    image_url='image_editor/img/crop.png',
                    id=attrs['id'],
                    filter_title=ugettext('Crop')
                )

    def render_initial(self, attrs, filter_name):
        return ""

    def proceed_image(self, image, params):
        width, height = image.size
        x_coef = float(width) / float(params['width'])
        y_coef = float(height) / float(params['height'])
        image = image.crop((
            int(params['x'] * x_coef), int(params['y'] * y_coef), int(params['x2'] * x_coef), int(params['y2'] * y_coef)))
        return image