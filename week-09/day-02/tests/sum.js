'use strict'

class Sum {
    sumNumbers(list) {
        if (list.length === 0) {
            list = [0];
        }
        let sumNumber = list.reduce(function(sum, value) {
            return sum + value;
        })
    return sumNumber;
    }
};

module.exports = Sum;

