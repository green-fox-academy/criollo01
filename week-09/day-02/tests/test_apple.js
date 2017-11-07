'use strict'

var test = require('tape');
var returnApple = require('./apple');

test("something", function(t) {
    t.equal(returnApple(), 'apple');
    t.end();
})