(function($) {
    // http://teamdf.com/jquery-plugins/license/
    $.fn.visible = function(partial) {
        var $t = $(this),
            $w = $(window),
            viewTop = $w.scrollTop(),
            viewBottom = viewTop + $w.height(),
            _top = $t.offset().top,
            _bottom = _top + $t.height(),
            compareTop = partial === true ? _bottom : _top,
            compareBottom = partial === true ? _top : _bottom;
        return ((compareBottom <= viewBottom) && (compareTop >= viewTop));
    };
})(jQuery);

function animateCardSlideInUp() {
    $('.dashboard-card').each(function(i, el) {
        if ($(el).visible(true)) {
            $(el).addClass('animated slideInUp');
        }
    });
}

$(function() {
    $(".owl-carousel").owlCarousel({
        animateOut: 'slideOutRight',
        animateIn: 'flipInY',
        autoplay: true,
        autoplayTimeout: 2000,
        lazyLoad: true,
        // autoplayHoverPause: 3000,
        // center: true,
        items: 1,
        rtl: true,
        loop: true,
        margin: 10,
        nav: true,
        dots: true,
        stagePadding: 50,
        smartSpeed: 450,
        // responsive: {
        //     0: {
        //         items: 1,
        //     },
        //     600: {
        //         items: 2,
        //     }
        // }
    });
    $('[data-toggle="tooltip"]').tooltip();
    var nanobar = new Nanobar();
    nanobar.go(100);
    animateCardSlideInUp();

    $('#people-you-may-follow').addClass('animated slideInRight');
    $('#random-quote').addClass('animated zoomIn');

    $(window).on('scroll', function(event) {
        animateCardSlideInUp();
    });
});

