/* Function to open the camera*/


function openFun() {

    var video = document.getElementById('video');

    // Get access to the camera!
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Not adding `{ audio: true }` since we only want video now
        navigator.mediaDevices.getUserMedia({
            video: true
        }).then(function (stream) {
            //video.src = window.URL.createObjectURL(stream);
            video.srcObject = stream;
            video.play();
        });
    }

}


/*<!--#############################################################################################################-->*/




/* Function to close the camera*/

function vidOff() {
    const video = document.querySelector('video');

    // A video's MediaStream object is available through its srcObject attribute
    const mediaStream = video.srcObject;

    // Through the MediaStream, you can get the MediaStreamTracks with getTracks():
    const tracks = mediaStream.getTracks();

    // Tracks are returned as an array, so if you know you only have one, you can stop it with: 
    tracks[0].stop();

    // Or stop all like so:
    tracks.forEach(track => track.stop())
}




/*<!--#############################################################################################################-->*/


/* Function to take photo and matching it */

$(function () {
    var canvas = document.getElementById('canvas');
    var data_pixel = canvas.getContext('2d').getImageData(0, 0, 640, 480).data;
    
    $('.form1').submit(function (e) {
        // let serialize = $(this).serialize();
        let $form = $(".form1");
        let $form_data = new FormData($form[0]);
        let url = $(this).data('url')
        // console.log(serialize)
        $.ajax({
            method: "POST",
            url: url,
            data: { 'data':form_data,'image': JSON.stringify(data_pixel) },
            success: function (response) {
                console.log(response)
            }

        });

    });




});


function photoFun() {
    // Elements for taking the snapshot

    var video = document.getElementById('video');

}


/*<!--#############################################################################################################-->*/



/* Attendance registration */


function attendance() {

    var id = document.getElementById('id').innerHTML;

    if (id != "No Element") {
        var table = document.getElementById("myTable");

        var row = table.insertRow(1);

        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);

        var today = new Date();

        var dateTime = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate() + ' / ' + today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

        cell1.innerHTML = dateTime;
        cell2.innerHTML = id;
        cell3.innerHTML = document.getElementById('name').innerHTML;
        cell4.innerHTML = document.getElementById('level').innerHTML;
        cell5.innerHTML = document.getElementById('dep').innerHTML;


        document.getElementById('id').innerHTML = "No Element";
        document.getElementById('name').innerHTML = "No Element";
        document.getElementById('level').innerHTML = "No Element";
        document.getElementById('dep').innerHTML = "No Element";
    } else {
        alert("This student is not registered or the picture is not clear");
    }

}

/*<!--#############################################################################################################-->*/