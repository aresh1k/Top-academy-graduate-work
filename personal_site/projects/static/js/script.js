var messages = document.getElementsByClassName('messages');

setTimeout(function(){
    for (var i = 0; i < messages.length; i++) {
    messages[i].remove();
    }
}, 3000);