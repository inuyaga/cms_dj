$(function () {
    $.scrollUp({
        animation: 'fade',
        activeOverlay: '#00FFFF',
        scrollImg: true
    });
});
$(window).on('scroll', function(){
    if($(window).scrollTop() > 50){
        $('#principalnav').css({
            position: 'fixed',
            top: '0px',
            left : '0px',
            width: '100%',
            zIndex: 1,
            WebkitTransition : ' all 150ms ease-in-out',
            MozTransition    : ' all 150ms ease-in-out',
            MsTransition     : ' all 150ms ease-in-out',
            OTransition      : ' all 150ms ease-in-out',
            transition       : ' all 150ms ease-in-out'
        });
        $('#imglogo').css({
            width:"55",
            height:"70",
            WebkitTransition : ' all 150ms ease-in-out',
            MozTransition    : ' all 150ms ease-in-out',
            MsTransition     : ' all 150ms ease-in-out',
            OTransition      : ' all 150ms ease-in-out',
            transition       : ' all 150ms ease-in-out'
        });
        $("#principalnav").fadeIn();
        $("#segundaNav").hide("slow");
    }else{
        $('#principalnav').css({
            position: 'relative',
            top: '0px',
            width: '100%',
            zIndex: 1,
            WebkitTransition : ' all 150ms ease-in-out',
            MozTransition    : ' all 150ms ease-in-out',
            MsTransition     : ' all 150ms ease-in-out',
            OTransition      : ' all 150ms ease-in-out',
            transition       : ' all 150ms ease-in-out'
        });
        
        $('#imglogo').css({
            width:"110",
            height:"140",
            WebkitTransition : ' all 150ms ease-in-out',
            MozTransition    : ' all 150ms ease-in-out',
            MsTransition     : ' all 150ms ease-in-out',
            OTransition      : ' all 150ms ease-in-out',
            transition       : ' all 150ms ease-in-out'
        });
        $("#segundaNav").show("slow");
    }
});


function ConteoRegresivo()
{//año/mes del año (comenzando con el mes 0)/dia/hora
    var fecha=new Date('2019','7','31','08','00','00');
    var hoy=new Date();
    var dias=0;
    var horas=0;
    var minutos=0;
    var segundos=0;
    if (fecha>hoy)
    {
        var diferencia=(fecha.getTime()-hoy.getTime())/1000;
        dias=Math.floor(diferencia/86400);
        diferencia=diferencia-(86400*dias);
        horas=Math.floor(diferencia/3600);
        diferencia=diferencia-(3600*horas);
        minutos=Math.floor(diferencia/60);
        diferencia=diferencia-(60*minutos);
        segundos=Math.floor(diferencia);
        document.getElementById('contador').innerHTML = '<div class="row"><div class="col-md-3 text-center">' + dias + '<br><span style="font-size: 50%;">Días</span></div><div class="col-md-3 text-center">' + horas + '<br><span style="font-size: 50%;">Horas</span></div><div class="col-md-3 text-center">' + minutos + '<br><span style="font-size: 50%;">Minutos</span></div><div class="col-md-3 text-center">' + segundos + '<br><span style="font-size: 50%;">Segundos</span></div></div>';
        if (dias>0 || horas>0 || minutos>0 || segundos>0)
        {
            setTimeout("ConteoRegresivo()",1000)
        }
    }
    else
    {
        document.getElementById('contador').innerHTML = '0 Días ¡Comenzó!';
    }
}

$(document).ready(function () {
    ConteoRegresivo();
    $('#myModal').modal('show');
});

(function pulse(back) {
    $('#pulse1').animate( {
         'border-style': (back) ? 'dotted' : 'solid',
         'border-width':(back) ? '1px':'10px',
         opacity: (back) ? 1 : 0.1 
        }, 1000, function(){
            pulse(!back)
        }); 
    })
(false);
(function pulse(back) {
     $('#pulse2').animate( {
          'font-size': (back) ? '100px' : '140px', opacity: (back) ? 1 : 0.5 
        }, 700, function(){
            pulse(!back)}); 
        }
)(false); 