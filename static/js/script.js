$(document).ready(function() {
    // Fading Backgrounds

    // Credits to rudolfson.junior for his tutorial on Youtube
    // https://www.youtube.com/watch?v=XjPdQSqtJhs
    // Thank you for the great explanation!

    var count = Math.floor(Math.random() * 3);


    console.log('count at first: ' + count);
    var images = [
        "../static/images/backgrounds/bg1.jpg",
        "../static/images/backgrounds/bg2.jpg",
        "../static/images/backgrounds/bg3.jpg",
        "../static/images/backgrounds/bg4.jpg",
    ];

    var image = $(".fader");
    image.css("background-image", "url(" + images[count] + ")");
    console.log('count now: ' + count);

    setInterval(function() {
        

        image.fadeOut(1000, function() {

            console.log('old count: ' + count);
            var oldcount = count;
            while (count == oldcount){
                count = Math.floor(Math.random() * 4);
            }
            

            // New picture presents defined on new count
            image.css("background-image", "url(" + images[count] + ")");
            console.log('new picture presents: ' + count);
            image.fadeIn(1000);
        });
        
    }, 10000);
});