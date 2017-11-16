'use strict'

const url = "http://localhost:3000";

function ajax (method, url, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.onload = function() {
    console.log(xhr.responseText);
      callback(JSON.parse(xhr.responseText));
    };
    xhr.send();
  };

function appendToBody(element) {
    let someElement = document.createElement("p");
    someElement.innerText = element;
    document.body.appendChild(someElement);
}

function listBookTitles(result){
    result.forEach(element => {
        appendToBody(element);
    });
}

ajax('GET', url + '/allbooks', listBookTitles)