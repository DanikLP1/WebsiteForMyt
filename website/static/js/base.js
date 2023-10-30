jQuery(function() {
    jQuery('#load-more').click(function() {
      var page = parseInt(jQuery(this).attr('data-page')) + 1;
      jQuery.ajax({
        url: '/',
        data: {
          'page': page
        },
        dataType: 'json',
        success: function(data) {
          if (data.length > 0) {
            jQuery('#feedback-list').append(data);
            jQuery('#load-more').attr('data-page', page);
          } else {
            jQuery('#load-more').hide();
          }
        }
      });
    });
  });