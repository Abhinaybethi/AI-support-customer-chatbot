// voice.js
let recognition;
let isListening = false;

function startListening(callback) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.start();
    isListening = true;

    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        callback(transcript);
    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error", event.error);
    };

    recognition.onend = function () {
        isListening = false;
    };
}

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    window.speechSynthesis.speak(utterance);
}

export { startListening, speak };
