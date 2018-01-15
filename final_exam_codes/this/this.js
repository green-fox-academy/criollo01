'use strict'

let talk = function () {
    console.log(this.sound);
};

let boromir = {
    speak: talk,
    sound: 'One does not simply walk into mordor'
};

boromir.speak()
talk()