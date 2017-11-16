'use strict';

var express = require('express');
var mysql = require('mysql');

var app = express();
app.use('/assets', express.static('./assets'));

var connection = mysql.createConnection({
  host : 'localhost',
  user: 'root',
  password: 'a',
  database: 'bookstore'
});
connection.connect();

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
})

app.get('/allbooks', function(req, res) {
    var allBooksTitle = [];
    connection.query('SELECT book_name FROM book_mast', function(err, result, request) {
        result.forEach(element => {
            allBooksTitle.push(element.book_name);
        });
    res.send(allBooksTitle);
    })
})

app.listen(3000, () => console.log("server running"));
