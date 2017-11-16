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

var books = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';

app.get('/allbooks', function(req, res) {
    var allBooksTitle = [];
    connection.query('SELECT book_name FROM book_mast', function(err, result, request) {
        result.forEach(element => {
            allBooksTitle.push(element.book_name);
        });
    res.send(allBooksTitle);
    })
})

app.get('/allbookdata', function(req, res) {
    connection.query(books, function(err, data) {
        if (err) {
            console.log(err.toString);
        }
        res.send({'books': data});
    })
    console.log('Data received from database');
})

app.listen(3000, () => console.log("server running"));
