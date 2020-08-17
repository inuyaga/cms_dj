//  document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.sidenav');
//     var instances = M.Sidenav.init(elems);
//   });
// $('.cardgiratoria').click(function(){
//     $(this).toggleClass('flipped');
//     });
$(".cardgiratoria").flip({axis: 'x'});
    // $( ".cardgiratoria" ).hover(
    //     function() {
    //         $(this).toggleClass('flipped');
    //     }
    //   );
$(document).ready(function(){
    $('.sidenav').sidenav();
	$(".dropdown-trigger").dropdown();
	$('.carousel.carousel-slider').carousel({
		fullWidth: true,
		indicators: false
	});
	$('.modal').modal();
	$('.parallax').parallax();
    $('.collapsible').collapsible();
    $('.tabs').tabs();
  });
$(window).on('scroll', function(){
    if($(window).scrollTop() > 50){
        $('#modBarra').css({
            position: 'fixed',
            top: '0px',
            left : '0px',
            // width: '100%',
            zIndex: 1000,
            WebkitTransition : ' all 300ms ease-in-out',
            MozTransition    : ' all 300ms ease-in-out',
            MsTransition     : ' all 300ms ease-in-out',
            OTransition      : ' all 300ms ease-in-out',
            transition       : ' all 300ms ease-in-out'
        });
        // $("#modBarra").fadeIn("slow");
        $("#modBarra").slideDown("slow");
        $('#imglogo').css({
            width:"25",
            height:"38.75",
            zIndex:1,
            WebkitTransition : ' all 150ms ease-in-out',
            MozTransition    : ' all 150ms ease-in-out',
            MsTransition     : ' all 150ms ease-in-out',
            OTransition      : ' all 150ms ease-in-out',
            transition       : ' all 150ms ease-in-out'
        });
        $('#mobile-demo').css({
            zIndex:1001,
        });
        $("#barraIdioma").hide("slow");
    }else{
        $('#modBarra').css({
            position: 'relative',
            top: '0px',
            // width: '100%',
            zIndex: 1000,
            WebkitTransition : ' all 300ms ease-in-out',
            MozTransition    : ' all 300ms ease-in-out',
            MsTransition     : ' all 300ms ease-in-out',
            OTransition      : ' all 300ms ease-in-out',
            transition       : ' all 300ms ease-in-out'
        });
        $('#imglogo').css({
            width:"70",
            height:"77.5",
            zIndex:1,
            WebkitTransition : ' all 150ms ease-in-out',
            MozTransition    : ' all 150ms ease-in-out',
            MsTransition     : ' all 150ms ease-in-out',
            OTransition      : ' all 150ms ease-in-out',
            transition       : ' all 150ms ease-in-out'
        });
        $('#mobile-demo').css({
            zIndex:1001,
        });
        $("#barraIdioma").show("slow");
    }
});