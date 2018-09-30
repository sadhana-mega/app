var audio_context;
var recorder;

function startUserMedia(stream) {
    var input = audio_context.createMediaStreamSource(stream);
    console.log('Media stream created.');
    recorder = new Recorder(input);
    console.log('Recorder initialised.');
}

function startRecording() {
    recorder && recorder.record();
    console.log('Recording...');
}

function stopRecording() {
    recorder && recorder.stop();
    console.log('Stopped recording.');
    recorder && recorder.exportWAV(function (blob) {
        var data = new FormData();
        var file = new File([blob], 'test.wav', {
            'type': 'audio/wav'
        });
        data.append('file', file);
        $.ajax({
            url: "/upload",
            type: 'POST',
            data: data,
            contentType: false,
            processData: false,
            success: function (data) {
                transcript = data.transcript;
                input = []
                confidence_sum = 0;
                for(i=0; i<transcript.words.length; i++)
                {
                    input.push(transcript.words[i].text);
                    confidence_sum += transcript.words[i].confidence;
                }
                clarity = confidence_sum / input.length;
                console.log(input);
                given_words = $("#para").html().trim().split(" ");
                console.log(given_words);
                word_score = 0;
                for (var i = 0; i < input.length; i++) {
                    var para = document.createElement('span');
                    var text = document.createTextNode(input[i] + " ");
                    para.appendChild(text);
                    if (given_words[i].toLowerCase() === input[i].toLowerCase())
                    {
                        para.className = "correct";
                        word_score++;
                    }
                    else if (given_words[i].toLowerCase() !== input[i].toLowerCase())
                    {
                        para.className = "incorrect";
                    }
                    document.querySelector('.result').appendChild(para);
                }
                $("#word-score").html("Word Score: " + word_score.toString());
                clarity_percentage = Math.round(clarity * 100);
                $("#clarity").html("Clarity: " + clarity_percentage + "%");
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
    recorder.clear();
}

$(document).ready(function () {
    try {
        window.AudioContext = window.AudioContext || window.webkitAudioContext;
        navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
        window.URL = window.URL || window.webkitURL;

        audio_context = new AudioContext;
        console.log('Audio context set up.');
        console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
        alert('No web audio support in this browser!');
    }

    navigator.getUserMedia({
        audio: true
    }, startUserMedia, function (e) {
        console.log('No live audio input: ' + e);
    });

    $("#start").click(function () {
        startRecording();
    });

    $("#stop").click(function () {
        stopRecording();
    });
});