## -*- coding: utf-8 -*- ####################################################

from django.conf import settings
from django.forms.widgets import Widget, Media
from django.template.loader import render_to_string

from image_editor.settings import FILTER_CLASSES

class ImageEditWidget(Widget):

    def _get_media(self):
        media = Media(
            css={ 'all': ('image_editor/css/image_editor.css', ) },
            js = ('image_editor/js/image_editor.js', 'image_editor/js/jquery.json.js')
        )
        for n, f in FILTER_CLASSES.items():
            media = media + f.media
        return media
    media = property(_get_media)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = value
        buttons = {}
        initials = []
        for name, filter in FILTER_CLASSES.items():
            button = filter.render_button(attrs=final_attrs, filter_name=name)
            if button:
                buttons[name] = button
            initials.append(filter.render_initial(attrs=final_attrs, filter_name=name))
        final_attrs.update({
            'STATIC_URL': getattr(settings, 'STATIC_URL', settings.MEDIA_URL),
            'buttons': buttons,
            'initials': initials
        })
        return render_to_string('image_editor/image_editor_widget.html', final_attrs)

