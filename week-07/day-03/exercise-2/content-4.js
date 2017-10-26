    // 1) replace the list items' content with items from this list:
    // ['apple', 'banana', 'cat', 'dog']
    // 2) change the <ul> element's background color to 'limegreen'
    //   - don't just add a CSS class
    //   - use the .style attribute

let list = document.querySelectorAll('li');
let listContent = ['apple', 'banana', 'cat', 'dog'];

for (let i = 0; i < listContent.length; i++) {
    list[i].textContent = listContent[i];
}

let ul = document.querySelector('ul');
ul.setAttribute('style', 'background-color: limegreen');