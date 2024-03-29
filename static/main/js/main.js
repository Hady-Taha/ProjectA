//open the camera
function openFun() {
  var video = document.getElementById("video");

  // Get access to the camera!
  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices
      .getUserMedia({
        video: true,
      })
      .then(function (stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
      });
  }
}


//close the camera
function vidOff() {
  const video = document.querySelector("video");

  // A video's MediaStream object is available through its srcObject attribute
  const mediaStream = video.srcObject;

  // Through the MediaStream, you can get the MediaStreamTracks with getTracks():
  const tracks = mediaStream.getTracks();

  // Tracks are returned as an array, so if you know you only have one, you can stop it with:
  tracks[0].stop();

  // Or stop all like so:
  tracks.forEach((track) => track.stop());
}


//take photo and matching it 
function photoFun() {
  // Elements for taking the snapshot
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext("2d");
  var video = document.getElementById("video");
  // Trigger photo take
  context.drawImage(video, 0, 0, 250, 250);
  // console.log(covertData());
}


//convert photo to base64
function covertData() {
  var canvas = document.getElementById("canvas");
  var dataurl = canvas.toDataURL();

  return dataurl
}


//convert register photo to base64
function coverRegistertData() {
  var canvas = document.getElementById("registerCanavas");
  var dataurl = canvas.toDataURL();

  return dataurl
}




//send photo base64 to server 
$(function () {

  $(".sendToServer").submit(function (e) {

    e.preventDefault();
    let url = $(this).data('url')
    let token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: url,
      data: {
        csrfmiddlewaretoken: token,
        data: covertData(),
      },
      success: function (response) {
        alert("done");
      },
    });

    $(".sendRegiserData").submit(function (e) {

      e.preventDefault();
      let url = $(this).data('url')
      let token = $("input[name=csrfmiddlewaretoken]").val();
  
      $.ajax({
        type: "POST",
        url: url,
        data: {
          csrfmiddlewaretoken: token,
          data: coverRegistertData(),
        },
        success: function (response) {
          alert("done");
        },
      });
  });







  //csrfmiddlewaretoken‏
}); 
