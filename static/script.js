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
                console.log(data);
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

    $("#start").click(function(){
        startRecording();
    });

    $("#stop").click(function(){
        stopRecording();
    });
});