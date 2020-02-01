$(document).ready(function () {

    // Upon the document loading, assign two different navbar styles  to width below and above 800.
    // Below 800, assign a static top class. Above 800, assign a transparent background that picks up color after the user has scrolled for 20 pixels.

        $("#navbar").removeClass("static-top bg-color").addClass("fixed-top bg-transparent");

        $(window).scroll(function () {
            $("nav").toggleClass('scrolled', $(this).scrollTop() > 20);        });


});