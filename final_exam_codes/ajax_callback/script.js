'use strict'

let xhr = new XMLHttpRequest();
let url = 'https://api.giphy.com/v1/gifs/search?api_key=mAjsye6MxUqXDSoBF5y8iAMbsA8TMBEu&q=lavalamp&limit=10&offset=0&rating=G&lang=en'

function ajax(callback) {
  xhr.open('GET', url);
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      callback(JSON.parse(xhr.responseText));
    };
  };
};

function showStillGif(gifData) {
  for (let i = 0; i < 10; i++) {
    let newGif = document.createElement('img');
    newGif.setAttribute('src', gifData.data[i].images.fixed_height_still.url);
    document.body.insertAdjacentElement('beforeend', newGif);
    newGif.setAttribute('data-alt', gifData.data[i].images.fixed_height.url);
    gifMovement(newGif);
  };
};

function gifMovement(image, gif){
  image.addEventListener('click', function(){
    [this.src, this.dataset.alt] = [this.dataset.alt, this.src];
  });
};

window.onload = function() {
    ajax(showStillGif);
};