$(document).ready(function () {
    var scroll_pos = 0;
    $(document).scroll(function () {
        scroll_pos = $(this).scrollTop();
        if (scroll_pos > 30) {
            $("#mainNav").addClass("scrolled");

        } else {
            $("#mainNav").removeClass("scrolled");
        }
    });
});


const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
    $('#message').fadeOut('slow');
}, 5000);

