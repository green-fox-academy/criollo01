'use strict';

const test = require('tape');
const script = require('./script');

test('counting elements of array', (t) => {
  let fruits = ['apple', 'banana', 'melon', 'strawberry', 'raspberry'];
  t.equal(script.arrayCounter(fruits),5);
  t.end();
});

test('add two numbers', (t) => {
  t.equal(script.addElements(5,5), 10);
  t.end();
});
