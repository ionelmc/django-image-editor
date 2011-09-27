(function($){
    $.fn.cropper = function(id, options){
        var button = $(this),
            container = $('#' + id),
            image = container.find('img.edited_image'),
            crop_api = null;

        button.click(function(e){

            if(!crop_api){
                crop_api = $.Jcrop(image, {});
                image.Jcrop(options);
                if (options.initialCoords) {
                    crop_api.setSelect(options.initialCoords);
                }

                container.find('.tmp_tools')
                         .html('<a href="#" class="crop_apply">Apply</a>&nbsp;&nbsp;<a href="#" class="crop_cancel">Cancel</a>')
                         .find('.crop_apply').click(function(){
                             var params = crop_api.tellSelect();
                             crop_api.destroy();
                             crop_api = null;
                             params.width = image.width();
                             params.height = image.height();
                             image_editor.apply('crop', params);
                            
                             $(this).parent().html('');
                             return false;
                         }).parent()
                         .find('.crop_cancel').click(function(){
                             crop_api.destroy();
                             crop_api = null;
                             $(this).parent().html('');
                             return false;
                         });
            }
            return false;
        });
    };
})(jQuery);