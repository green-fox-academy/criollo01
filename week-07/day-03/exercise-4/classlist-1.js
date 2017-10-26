    // Does the third p have a red-dot class?
    // If so, alert 'OMG DOTS!'
    // If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
    // If the first p has an 'apple' class, replace cat's content with 'dog'
    // Make apple red by adding a .red class
    // Make balloon less balloon-like

let paragraphs = document.querySelectorAll('p');

if (paragraphs[2].classList.contains('red-dot')) {
    alert('OMG DOTS!');
}

if (paragraphs[3].classList.contains('dolphin')) {
    paragraphs[0].textContent = 'pear';
}

if (paragraphs[0].classList.contains('apple')) {
    paragraphs[2].textContent = 'dog';
}

paragraphs[0].classList.add('.red');

