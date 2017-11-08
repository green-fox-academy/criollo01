let express = require('express');
let app = express();
let bodyParser = require('body-parser');
let parser = bodyParser.urlencoded({extended :false});

app.use('/assets', express.static('assets'));
app.use(bodyParser.json());

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(req, res){
    if (req.query.input) {
        res.json({
            "received" : req.query.input, "result" : req.query.input*2
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

app.post('/dountil/:item', parser, function(req, res) {
    if (req.params.item == "sum") {
        let sumOf = 0;
        let number = req.body.until;
        while (number > 0){
            sumOf += number;
            number--;
        } 
        res.json({"result" : sumOf});
    } else if (req.params.input === "factor") {
        let num = req.body.until;
        let fact = 1;
        while (num > 0){
            fact *= num;
            num--;
        }
        res.json({"result" : fact});
    } else if (req.params.input === '') {
        res.json({
            "error" : "Please provide a number!"            
        });
    }
});

app.listen(8080);