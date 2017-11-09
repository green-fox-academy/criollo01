'use strict'

const express = require('express');
const app = express();
const mysql = require('mysql');

app.use(express.json());
app.use('/assets', express.static('./assets'));
express.json.type = "application/json";

const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'a',
    database: 'bookstore'
});

conn.connect(function(err){
    if(err){
        console.log("Error connecting to Db");
    } else {
        console.log("Connection established");
    }
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/title', function(req, res) {
    conn.query("SELECT book_name FROM book_mast;", function(err, result){
        if (err) {
            console.log(error.toString());
        }
        res.json(result);
    });
})

app.listen(8080);

