$(document).ready(function() {
    // Fading Backgrounds

    // Credits to rudolfson.junior for his tutorial on Youtube
    // https://www.youtube.com/watch?v=XjPdQSqtJhs
    // Thank you for the great explanation!

    var count = Math.floor(Math.random() * 9);
    var images = [
        "/static/images/backgrounds/bg1.jpg",
        "/static/images/backgrounds/bg2.jpg",
        "/static/images/backgrounds/bg3.jpg",
        "/static/images/backgrounds/bg4.jpg",
        "/static/images/backgrounds/bg5.jpg",
        "/static/images/backgrounds/bg6.jpg",
        "/static/images/backgrounds/bg7.jpg",
        "/static/images/backgrounds/bg8.jpg",
        "/static/images/backgrounds/bg9.jpg"];

    var image = $(".fader");
    image.css("background-image", "url(" + images[count] + ")");

    setInterval(function() {

        image.fadeOut(1000, function() {
            var oldcount = count;
            while (count === oldcount) {
                count = Math.floor(Math.random() * 9);
            }

            // New picture presents defined on new count
            image.css("background-image", "url(" + images[count] + ")");
            image.fadeIn(1000);
        });

    }, 10000);

    // Toggle themes

    $('.theme').click(function() {
        $(this).toggleClass("down");
        if ($(this).children().val() == "false") {
            $(this).children().val("true");
        } else {
            $(this).children().val("false");
        }
    });

    // Validate form when adding an assignment and call Modal if valid

    $("#submitAssignmentButton").click(function() {
        var title = document.forms["add_assignment"]["title"].value
        var short_description = document.forms["add_assignment"]["short_description"].value
        var long_description = document.forms["add_assignment"]["long_description"].value
        var location = document.forms["add_assignment"]["location"].value
        var end_date = document.forms["add_assignment"]["end_date"].value

        if ((title == "") || (short_description == "") || (long_description == "") || (location == "") || (end_date == "")) {
            document.forms['add_assignment'].reportValidity()
        } else {
            $('#add_assignment_modal').modal('show')
        }
    });

    // Validate form when adding a proposal and call Modal if valid

    $("#submitProposalButton").click(function() {
        var title = document.forms["add_proposal"]["title"].value
        var description = document.forms["add_proposal"]["description"].value
        var materials = document.forms["add_proposal"]["materials"].value
        var techniques = document.forms["add_proposal"]["techniques"].value
        var availability_start = document.forms["add_proposal"]["availability_start"].value
        var availability_end = document.forms["add_proposal"]["availability_end"].value

        if ((title == "") || (description == "") || (materials == "") || (techniques == "") || (availability_start == "") || (availability_end == "")) {
            document.forms['add_proposal'].reportValidity()
        } else {
            $('#add_proposal_modal').modal('show')
        }


    });

    // Scroll to section

    $("#howdoesclick").click(function(e) {
        e.preventDefault();
        var section = $(this).attr("href");
        $("html, body").animate({
            scrollTop: $(section).offset().top
        });
    });
});