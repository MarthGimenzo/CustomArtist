$(document).ready(function(){
  
    // Fading Backgrounds
    
    // Credits to rudolfson.junior for his tutorial on Youtube
    // https://www.youtube.com/watch?v=XjPdQSqtJhs
    // Thank you for the great explanation!

var count = 2;
var images = ["../static/images/backgrounds/bg1.jpg",
            "../static/images/backgrounds/bg2.jpg",
            "../static/images/backgrounds/bg3.jpg",
            "../static/images/backgrounds/bg4.jpg"];


var image = $(".fader")


  setInterval(function(){
    image.fadeOut(1000, function(){
      image.css("background-image","url("+images[count++]+")");
      image.fadeIn(1000);
      
    });
    if(count == images.length)
    {
      count = 0;
    }
  },10000);



});