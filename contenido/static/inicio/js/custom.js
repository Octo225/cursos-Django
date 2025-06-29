$(document).ready(function() {
    // Highlight active menu item
    var current = location.pathname;
    $('.navbar-nav li a').each(function() {
        var $this = $(this);
        if (current.indexOf($this.attr('href')) {
            $this.parent().addClass('active');
        }
    });
    
    // Smooth scrolling for anchor links
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault();
        
        $('html, body').animate(
            {
                scrollTop: $($(this).attr('href')).offset().top - 70,
            },
            500,
            'linear'
        );
    });
    
    // Close mobile menu when clicking on item
    $('.navbar-nav li a').on('click', function() {
        if ($(window).width() < 992) {
            $('.navbar-toggle').click();
        }
    });
});