'use strict';

function articles(callback){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=1fc7a7dbfaee49a7b9012a13b9bee39b&begin_date=19690719&end_date=19690720');
    xhr.onload = function(){
        let articles = JSON.parse(xhr.responseText);
        console.log(articles);
        callback(articles);
    }
    xhr.send();
}

function getArticles(input) {
    let h1 = document.createElement('h1');
    let snippet = document.createElement('article');
    let published = document.createElement('p');
    let permalink = document.createElement('a');

    h1.textContent = input.response.docs[5].headline.main;
    snippet.textContent = input.response.docs[5].snippet;
    permalink.textContent = 'Read More';
    permalink.href = input.response.docs[5].web_url;
    published.textContent = 'Published: ' + input.response.docs[5].pub_date;   
    
    document.body.appendChild(h1);
    document.body.appendChild(snippet);
    document.body.appendChild(permalink);
    document.body.appendChild(published);
}

articles(getArticles);