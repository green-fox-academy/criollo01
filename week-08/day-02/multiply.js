// Create the multiplier function that you can use like this:

const duplicator = multiplier(2);

function multiplier(x) {
    return function(y) {
        return x * y;
    };
}

console.log(duplicator(5)); // should log 10
console.log(duplicator(10)); // should log 20

const threeTimes = multiplier(3);

console.log(threeTimes(5)); // should log 15
console.log(threeTimes(100)); // should log 300

function greet(greeting) {
    return function(name) {
        console.log(greeting, name)
    }
}
var helloGreeter = greet('hello')
helloGreeter('Luca')
helloGreeter('István')
greet('hello')('István')

function multiply (x, y) {
    return x * y
}