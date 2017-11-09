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
        console.log("Mysql connection established");
    }
});



app.listen(8080);

