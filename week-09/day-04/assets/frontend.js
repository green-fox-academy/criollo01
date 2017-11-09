'use strict';

const url = 'http://localhost:8080/title';

function ajax (command, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open(command, url);
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            callback(JSON.parse(xhr.responseText));
            console.log(JSON.parse(xhr.responseText));
        };
    };
    xhr.send();
};

let renderBook = (function(item){
    item.forEach(function(item) {
        let tempBook = document.createElement('p');
        tempBook.innerText = item.book_name;
        document.body.appendChild(tempBook);
    })
});

ajax('GET', renderBook);
