'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function moreThanFour(students) {
    let moreThanFourCandy = [];
    for (let i = 0; i < students.length; i += 1) {
        if (students[i]['candies'] > 4) {
            moreThanFourCandy.push(students[i]['name']);
        }
    }
    return moreThanFourCandy;
}
function countCandies(students) {
    let candies = 0;
    for (let i = 0; i < students.length; i += 1) {
        candies += students[i]['candies'];
    }
    return candies;
}

function averageCandies(students) {
    return countCandies(students) / students.length;
}

console.log(moreThanFour(students))
console.log(averageCandies(students))