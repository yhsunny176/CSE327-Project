
// light box js

$('.portfolio_img_text').magnificPopup({
    delegate: '.img-link',
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
        enabled: true,
        navigateByImgClick: true,
        preload: [0, 1]
    },
    image: {
        tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
        titleSrc: function (item) {
            return item.el.attr('title') + '<small></small>';
        }
    }
});



// Preloader 
jQuery(window).on('load', function () {
    jQuery("#status").fadeOut();
    jQuery("#preloader").delay(450).fadeOut("slow");
});



// ===== Scroll to Top ==== //
$(window).scroll(function () {
    if ($(this).scrollTop() >= 100) {
        $('#return-to-top').fadeIn(200);
    } else {
        $('#return-to-top').fadeOut(200);
    }
});
$('#return-to-top').click(function () {
    $('body,html').animate({
        scrollTop: 0
    }, 500);
});

// post job


$(document).ready(function () {
    $(".post-drop").click(function () {
        $(".post-page-wrapper").slideToggle();
    });
    $('body').on('click', function (e) {
        if (!$('.post-drop').is(e.target)
            && $('.post-drop').has(e.target).length === 0
            && $('.open').has(e.target).length === 0
        ) {
            $('.post-page-wrapper').slideUp();
        }
    });
});

/*--- Responsive Menu Start ----*/

// menu fixed
$(window).scroll(function () {
    var window_top = $(window).scrollTop() + 1;
    if (window_top > 100) {
        $('.menu-items-wrapper').addClass('menu-fixed animated fadeInDown');
    } else {
        $('.menu-items-wrapper').removeClass('menu-fixed animated fadeInDown');
    }
});
