// Add an item that says 'The Green Fox' to the asteroid list.
// Add an item that says 'The Lamplighter' to the asteroid list.
// Add a heading saying 'I can add elements to the DOM!' to the .container.
// Add an image, any image, to the container.

let asteroidList = document.querySelector('ul.asteroids');
let newAsteroidFirst = document.createElement('li');
newAsteroidFirst.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroidFirst);

let newAsteroidSecond = document.createElement('li');
newAsteroidSecond.textContent = 'The Lamplighter';
asteroidList.appendChild(newAsteroidSecond);

let container = document.querySelector('.container');
let heading = document.createElement('h1');
heading.textContent = 'I can add elements in the DOM!';
container.appendChild(heading);

let image = document.createElement('img');
image.setAttribute('src', 'http://cdn.pcwallart.com/images/moose-size-car-wallpaper-4.jpg');
container.appendChild(image);
