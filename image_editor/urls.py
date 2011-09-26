## -*- coding: utf-8 -*- ####################################################
from django.conf.urls.defaults import *

urlpatterns = patterns('image_editor.views',
    url(r'^make-preview$', 'make_preview', name='make_preview'),
)