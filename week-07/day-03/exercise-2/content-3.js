    // fill output1 with the first paragraph's content, text only.
    // fill output2 with the first paragraph's content keeping the cat strong.

let firstParagraph = document.querySelector('p');
let paragraphOutput1 = document.querySelector('.output1');
let paragraphOutput2 = document.querySelector('.output2');
paragraphOutput1.innerHTML = firstParagraph.textContent;
paragraphOutput2.innerHTML = firstParagraph.innerHTML;