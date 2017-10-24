'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let length = 10;
let width = 20;
let height = 35;

let surfaceArea = 2 * (length * width + width * length + length * height);
console.log('Surface area: ' + surfaceArea);
let volume = length * width * height;
console.log('Volume: ' + volume);