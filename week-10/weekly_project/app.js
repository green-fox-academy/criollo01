'use strict'

const express = require('express');
const app = express();
app.use(express.json());
app.use('/assets', express.static('./assets'));

app.get('/', function (req, res){
    res.sendFile(__dirname + '/foxplayer.html')
});

app.get('/playlists', function(req, res) {
    res.json([
        { "id": 1, "title": "Favorites", "system": 1},
        { "id": 2, "title": "Music for programming", "system": 0},
        { "id": 3, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0},
    ])
})

app.get('/playlist-tracks', function(req, res) {
    res.json([
        {
            'id': 2, 
            'title': 'Sea of Dreams', 
            'artist': 'Oberhofer', 
            'duration': 4.12, 
            'path': '/assets/Oberhofer-Sea_of_Dreams.mp3',
        },
        {
            'id': 3,
            'title': 'Brennum allt',
            'artist': 'Úlfur Úlfur',
            'duration': 4.05,
            'path': '/assets/ulfur_ulfur.mp3',
        },
    ])
})

app.listen(8080, function() {
    console.log('The server is running.')
})