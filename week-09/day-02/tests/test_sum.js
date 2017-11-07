'use strict'

let test = require('tape');
let sum = require('./sum');

test("something", function(t) {
    let list1 = [1, 2, 3]
    let sumTheNums = new sum();
    t.equal(sumTheNums.sumNumbers(list1), 6);
    t.end();
})