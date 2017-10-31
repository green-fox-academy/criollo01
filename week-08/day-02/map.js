'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

var numbersOfE = fruits.map(function(fruit){
  let eNumber = 0;
  for (var i = 0; i < fruit.length; i++) {
    if (fruit[i] === 'e') {
      eNumber++;
    }
  }
  return eNumber;
})

console.log(numbersOfE)