
  'use strict'
    // 1. store the element that says 'The King' in the 'king' variable.
    // console.log it.
    // 2. store the element that contains the text 'The Conceited Man'
    // in the 'conceited' variable.
    // show the result in an 'alert' window.
    // 3. store 'The Businessman' and 'The Lamplighter'
    // in the 'businessLamp' variable.
    // console.log each of them.
    // 4. store 'The King' and 'The Conceited Man'
    // in the 'conceitedKing' variable.
    // alert them one by one.
    // 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
    // in the 'noBusiness' variable.
    // console.log each of them.
    // 6. store 'The Businessman' in the 'allBizniss' variable.
    // show the result in an 'alert' window.

let king = document.getElementById('b325');
console.log(king);

let conceited = document.querySelector('.b326');
alert(conceited);

let businessLamp = document.querySelectorAll('.big');
console.log(businessLamp[0].textContent + '\n' + businessLamp[1].textContent);

let conceitedKing = document.querySelectorAll('#b325, .b326');
conceitedKing.forEach(function(element) {
  alert(element.textContent);
});

let noBusiness = document.querySelectorAll('#b325, .b326, .b329');
noBusiness.forEach(function(element) {
  console.log(element.textContent);
});

let allBizniss = document.querySelector('p.big');
alert(allBizniss.textContent)