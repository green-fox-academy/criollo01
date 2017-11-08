let express = require('express');
let app = express();

app.use('/assets', express.static('assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(req, res){
    if (req.query.input) {
        res.json({
            'received' : req.query.input, 'result' : req.query.input*2
        });
    } else {
        res.json({
            'error' : "Please provide an input!"
        });       
    }
});

app.get('/greeter', function(req, res) {
    if (!req.query.name) {
        res.json({
            'error' : 'Please provide a name!'
        });
    } else if (!req.query.title) {
        res.json({
            'error' : 'Please provide a title!'
        });
    } else {
        res.json({
            'welcome_message' : 'Oh, hi there ' + req.query.name + ', my dear ' + req.query.title + '!'
        });
    }
});

app.get('/appendA/:input', function(req, res) {
    res.json({
        'appended' : req.params.input + 'a'
    })
});



app.listen(8080);