var slidenumber = 1;

$(document).ready(function(){
  $("#next").click( function() {slide(1)});
  $("#prev").click( function() {slide(-1)});
});

function slide(n){
    slidenumber = slidenumber + n
    if (slidenumber < 1){
        slidenumber = 2
    } else if (slidenumber > 2) {
        slidenumber = 1
    }
    $("#slide").attr("src", "{% static 'mainpage/img/1.jpg' %}");
    $("#numbertext").html(slidenumber+" / 2");
}