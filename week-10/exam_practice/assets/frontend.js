'use strict'

const url = "http://localhost:3000";
let tableElement = document.querySelector('table');


function ajax (method, url, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.onload = function() {
    console.log(xhr.responseText);
      callback(xhr.responseText);
    };
    xhr.send();
  };

function appendToBody(element) {
    let someElement = document.createElement("p");
    someElement.innerText = element;
    document.body.appendChild(someElement);
}

function listBookTitles(response) {
    response.forEach(element => {
        appendToBody(element);
    });
}

function listAllData(response) {
    let information = JSON.parse(response);
    information.books.forEach(element => {
        let tableData = '<tr><td>' + element.book_name + 
                        '</td><td>' + element.aut_name + 
                        '</td><td>' + element.cate_descrip + 
                        '</td><td>' + element.pub_name + 
                        '</td><td>' + element.book_price + 
                        '</td></tr>';
        tableElement.innerHTML += tableData;
    });
}

ajax('GET', url + '/allbookdata', listAllData)