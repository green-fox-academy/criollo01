'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

let codingHours = 6 * (17 *5);
console.log(codingHours);

let weeklyCoding = codingHours / 17;
console.log(weeklyCoding);

let codingPercentage = weeklyCoding / 52 * 100;
console.log(codingPercentage + '%');