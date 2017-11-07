'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let  addString = function(str1, str2, printStr){  
  let newStr = str1 + str2;
  printStr();
}

let printStr = function(str) {
  console.log(str);
}

try {
  addString(1234, 56789, 'printStr');
} catch (error) {
  if (typeof str1 != String || typeof str2 != String) {
    console.log('some of these words are not a string');
  }
}
