## -*- coding: utf-8 -*- ####################################################

import os
from django.conf import settings

EDITED_PREVIEWS_ROOT = getattr(settings, 'EDITED_PREVIEWS_ROOT', os.path.join('image_editor', 'previews'))

IMAGE_EDITOR_FILTERS = getattr(settings, 'IMAGE_EDITOR_FILTERS', {
    'crop': 'image_editor.filters.crop_by_ratio.FixedRatioImageCropTool',
    'sepia': 'image_editor.filters.sepia.ImageSepiaFilter',
    'blur': 'image_editor.filters.blur.ImageBlurFilter',
    'sharpen': 'image_editor.filters.sharpen.ImageSharpenFilter',
    'contour': 'image_editor.filters.contour.ImageContourFilter',
    'edge_enhance': 'image_editor.filters.edge_enhance.ImageEdgeEnhanceFilter',
    'detail': 'image_editor.filters.detail.ImageDetailFilter',
})

FILTER_CLASSES = {}
for name, filter in IMAGE_EDITOR_FILTERS.items():
    chain = filter.split('.')
    FILTER_CLASSES[name] = getattr(__import__('.'.join(chain[:-1]), globals(), locals(), [chain[-1]]), chain[-1])()