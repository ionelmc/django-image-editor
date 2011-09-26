(function($){

    var make_select_ratio = function(){
        var html_code = '<label for="select_crop_ratio">Please, select crop ratio: </label><select id="select_crop_ratio">';
        for(var i = 0; i < image_editor_crop_ratios.length; i++){
            html_code += '<option value="' + image_editor_crop_ratios[i][0] + '">' + image_editor_crop_ratios[i][1] + '</option>';
        }

        return html_code + '</select><br/>';
    };

    $.fn.cropper = function(id){
        var button = $(this),
            container = $('#' + id),
            image = container.find('img.edited_image'),
            crop_api = null;

        button.click(function(e){

            if(!crop_api){
                crop_api = $.Jcrop(image, {});

                container.find('.tmp_tools')
                         .html(make_select_ratio() +
                               '<a href="#" class="crop_apply">Apply</a>&nbsp;&nbsp;<a href="#" class="crop_cancel">Cancel</a>')
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
                         }).parent()
                        .find('#select_crop_ratio').change(function(){
                            crop_api.destroy();
                            crop_api = $.Jcrop(image, {});
                            image.Jcrop({aspectRatio: $(this).find(':selected').val(), minSize: min_crop_sizes});
                        });
                image.Jcrop({aspectRatio: $('#select_crop_ratio :selected').val(), minSize: min_crop_sizes});
            }
            return false;
        });
    };
})(jQuery);