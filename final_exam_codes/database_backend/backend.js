'use strict'

const express = require('express');
const mysql = require('mysql');
const app = express();

app.use('/assets', express.static('./assets'));

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'a',
  database: 'licence_plates'
});

connection.connect(function(err) {
  if (err) {
    console.log('Can\'t connect to database');
  } else { 
    console.log('Connection established');
  };
});

app.get('/subaru', function(req, res) {
  let queryString = `SELECT * FROM licence_plates WHERE car_brand = 'Subaru'`;
  connection.query(queryString, (error, data) => {
    if (error) {
      console.log('Error in database query.');
    } else {
      res.send(data);
    }
  });
});

app.listen(8080, () => console.log('Server is running'));
