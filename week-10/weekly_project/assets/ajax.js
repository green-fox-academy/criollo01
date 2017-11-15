'use strict'

const ajax = function(){
    const xhr = new XMLHttpRequest();
    function api (method, url, content, callback) {
        xhr.open(method, url, true);
        xhr.onload = function() {
            var data = JSON.parse(xhr.responseText);
            console.log(data);
            callback(data);
        }
        xhr.send();
    }
}

