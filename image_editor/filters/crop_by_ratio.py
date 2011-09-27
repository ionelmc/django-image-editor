## -*- coding: utf-8 -*- ####################################################

from django.conf import settings
from django.utils.translation import ugettext
from django.utils import simplejson

from image_editor.filters.basic import ImageEditToolBasic

ratios_list = getattr(
    settings,
    'IMAGE_EDITOR_CROP_RATIOS',
    (
        (float('8') / 10, '8x10'),
        (float('10') / 8, '10x8'),
        (float('10') / 15, '10x15'),
        (float('15') / 10, '15x10'),
        (float('3') / 4, '3x4'),
        (float('4') / 3, '4x3'),
    )
)

min_crop_sizes = getattr(settings, 'IMAGE_EDITOR_MIN_CROP_SIZES', (100, 100))

class FixedRatioImageCropTool(ImageEditToolBasic):

    class Media:
        js = ('jcrop/js/jquery.Jcrop.min.js', 'jcrop/js/fixed_ratio_cropper.js')
        css = { 'all': ('jcrop/css/jquery.Jcrop.css', ) }

    def render_button(self, attrs, filter_name):
        return '<img src="%(static_url)s%(image_url)s" style="margin: 6px;" /><br/>%(filter_title)s \
                <script>$(function(){ $("#%(id)s_button_crop").cropper("%(id)s") });</script>' % \
               dict(
                    static_url=settings.STATIC_URL or settings.MEDIA_URL,
                    image_url='image_editor/img/crop.png',
                    id=attrs['id'],
                    filter_title=ugettext('Crop')
                )

    def render_initial(self, attrs, filter_name):
        return """<script>
            var image_editor_crop_ratios = %(crop_ratios)s,
                min_crop_sizes = %(min_size)s

        </script>""" % {
            'crop_ratios': simplejson.dumps(ratios_list),
            'min_size': simplejson.dumps(min_crop_sizes)
        }

    def proceed_image(self, image, params):
        width, height = image.size
        x_coef = float(width) / float(params['width'])
        y_coef = float(height) / float(params['height'])
        image = image.crop((
            int(params['x'] * x_coef), int(params['y'] * y_coef), int(params['x2'] * x_coef), int(params['y2'] * y_coef)))
        return image