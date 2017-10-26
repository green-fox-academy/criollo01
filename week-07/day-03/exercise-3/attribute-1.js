    // Write the image's url to the console.
    // Replace the image with a picture of your favorite animal.
    // Make the link point to the Green Fox Academy website.
    // Disable the second button.
    // Replace its text with 'Don't click me!'.

let imgSource = document.querySelector('img');
console.log(imgSource.getAttribute('src'));

imgSource.setAttribute('src', 'http://www.nhptv.org/wild/images/mooseusfwryanhagerty.jpg');

let link = document.querySelector('a');
link.setAttribute('href', 'https://www.greenfoxacademy.com/');

let secondButton = document.querySelector('.this-one');
secondButton.disabled = true;

secondButton.textContent = 'Don\'t click me!'