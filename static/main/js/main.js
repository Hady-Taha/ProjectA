$(function () {
    // Grab elements, create settings, etc.
    var video = document.getElementById('video');
    // Elements for taking the snapshot
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');

    document.getElementById('start').addEventListener("click", function () {
        // Get access to the camera!
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({
                video: true
            }).then(function (stream) {
                //video.src = window.URL.createObjectURL(stream);
                video.srcObject = stream;
                video.play();
            });
        }

        $('#snap').fadeIn();

        // Trigger photo take
        document.getElementById("snap").addEventListener("click", function () {
            context.drawImage(video, 0, 0, 640, 480);

            var dataURL = canvas.toDataURL();

            $("#use_image").click(function () {
                let $form = $(".image_submit_form");
                let form_data = new FormData($form[0]);

                $.ajax({
                    url: $form.attr('action'),
                    type: $form.attr('method'),
                    dataType: 'json',
                    data: JSON.stringify(dataURL),
                    data: {
                        imageBase64: dataURL
                    }
                }).done(function () {
                    console.log('sent');
                });
            });
        });

    });
})