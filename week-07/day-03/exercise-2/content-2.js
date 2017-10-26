// fill every paragraph with the last one's content.

'use strict'

let allParagraphs = document.querySelectorAll('p');
let lastParagraph = document.querySelector('.dog');
allParagraphs.forEach(function(e) {
    e.innerHTML = lastParagraph.innerHTML;
});