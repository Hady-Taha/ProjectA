/* Function to open the camera*/
$(function () {

  $('#openPhoto').click(function (e) {
    e.preventDefault();
    openFun()
  });


  $('#videoOff').click(function (e) {
    e.preventDefault();
    vidOff()
  });

  $('.done').submit(function (e) {
    e.preventDefault();
    let token = $('input[name=csrfmiddlewaretoken]').val()
    let url = $(this).data('url')
    
    $.ajax({
      type: "POST",
      url: url,
      data: { csrfmiddlewaretoken: token , data:photoFun() },
      success: function (response) {

      }
    });

    console.log(serialize);

  });






  
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


  var photoFun = function () {

    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var video = document.getElementById('video');
    context.drawImage(video, 0, 0, 600, 480);
    var dataURL = canvas.toDataURL();
    return dataURL;

  }


});










/*<!--#############################################################################################################-->*/