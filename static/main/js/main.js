
/* Function to open the camera*/


function openFun() 
{
    
   var video = document.getElementById('video');

    // Get access to the camera!
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia)
    {
        // Not adding `{ audio: true }` since we only want video now
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            //video.src = window.URL.createObjectURL(stream);
            video.srcObject = stream;
            video.play();
        });
    } 
    
}


        /*<!--#############################################################################################################-->*/




/* Function to close the camera*/

function vidOff() 
{
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

function photoFun() 
{
    // Elements for taking the snapshot
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var video = document.getElementById('video');

    // Trigger photo take

    context.drawImage(video, 0, 0, 600, 480);
    

    document.getElementById('id').innerHTML = "1111";
    document.getElementById('name').innerHTML = "Mostafa Amin";
    document.getElementById('level').innerHTML = "3 level";
    document.getElementById('dep').innerHTML = "CS";
    
}


        /*<!--#############################################################################################################-->*/



/* Attendance registration */


function attendance() {
    
    var id = document.getElementById('id').innerHTML;
    
    if(id != "No Element")
        {
              var table = document.getElementById("myTable");

              var row = table.insertRow(1);

              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              var cell3 = row.insertCell(2);
              var cell4 = row.insertCell(3);
              var cell5 = row.insertCell(4);

                var today = new Date();

                var dateTime = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate() + ' / ' + today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

              cell1.innerHTML = dateTime;
              cell2.innerHTML = id;
              cell3.innerHTML = document.getElementById('name').innerHTML;
              cell4.innerHTML = document.getElementById('level').innerHTML;
              cell5.innerHTML = document.getElementById('dep').innerHTML;
            
            
            document.getElementById('id').innerHTML = "No Element";
            document.getElementById('name').innerHTML = "No Element";
            document.getElementById('level').innerHTML = "No Element";
            document.getElementById('dep').innerHTML = "No Element";
        }
    
    else
    {
        alert("This student is not registered or the picture is not clear");
    }
 
}

        /*<!--#############################################################################################################-->*/








