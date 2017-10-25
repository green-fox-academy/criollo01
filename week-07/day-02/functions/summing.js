'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(number){
    var sumOfNumbers = 0; 
    for(let i = 0; i <= number; i++){
       sumOfNumbers += i;
    }
    return sumOfNumbers;
}

console.log(sum(5))