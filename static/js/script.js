$(document).ready(function () {
  // Fading Backgrounds

  // Credits to rudolfson.junior for his tutorial on Youtube
  // https://www.youtube.com/watch?v=XjPdQSqtJhs
  // Thank you for the great explanation!

  var count = Math.floor(Math.random() * 4);
  console.log(count);
  var images = [
    "../static/images/backgrounds/bg1.jpg",
    "../static/images/backgrounds/bg2.jpg",
    "../static/images/backgrounds/bg3.jpg",
    "../static/images/backgrounds/bg4.jpg",
  ];

  var image = $(".fader");
  image.css("background-image", "url(" + images[count] + ")");
  count++;

  setInterval(function () {
    image.fadeOut(1000, function () {
      console.log(count);
      image.css("background-image", "url(" + images[count++] + ")");
      console.log(count);
      image.fadeIn(1000);
    });
    if (count == images.length) {
      count = 0;
    }
  }, 10000);
});
