(function($){
    $.fn.image_editor = function(url, image_name, image_url){
        var operations = [],
            image_urls = [image_url],
            container = $(this).show(),
            image = container.find('img.edited_image').attr('src', image_url),
            image_wrapper = image.parent(),
            hidden_field = container.find('.image_editor_core_field'),
            undo_link = container.find('.image_edit_undo');

        var apply_changes = function(filter_name, params){
            operations.push({name: filter_name, params: params});
            hidden_field.val($.toJSON({ image: image_name, operations: operations }));
            refresh_image();
        };

        var refresh_image = function(){
            if(operations.length > image_urls.length - 1){
                get_image_url();
            } else {
                image.attr('src', image_urls[image_urls.length - 1]);
            }
            if(operations.length){
                undo_link.show()
            } else {
                undo_link.hide()
            }
        };

        var get_image_url = function(){
            image_wrapper.loadIndicator();
            $.post(url, {image: image_name, operations: $.toJSON(operations)}, function(data){
                if(data.success){
                    image_urls.push(data.image);
                } else {
                    alert(data.error);
                    operations.pop();
                }
                image_wrapper.deleteIndicator();
                refresh_image();
            });
        };

        var undo = function(){
            if(operations.length){
                operations.pop();
                image_urls.pop();
                hidden_field.val($.toJSON({ image: image_name, operations: operations }));
                refresh_image();
            }
        };

        container.find('.filter_auto_apply').parent().click(function(){
            var p = $(this).find('.filter_auto_apply');
            apply_changes(p.attr('filter_name'), p.attr('filter_params'));
            return false;
        });

        undo_link.click(function(){
            undo();
            return false;
        });

        return {
            'apply': apply_changes
        };
    }

    $.fn.loadIndicator = function(text) {
        //Append loader indicator
        var loader = $('<div class="loader">'+( text? '<div>'+text+'</div>' : '' )+'</div>');
        loader.height($(this).height());
        loader.width($(this).width());
        return $(this).before(loader).addClass('ajax-loading');
    };

    $.fn.deleteIndicator = function() {
        //Erase loader indicator
        $(this).removeClass('ajax-loading').prev('div.loader').remove();
    };
})(jQuery)