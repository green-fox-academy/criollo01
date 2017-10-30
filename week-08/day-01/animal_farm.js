class Animal {

    constructor(hunger, thirst) {
        this.hunger = 5;
        this.thirst = 5;
        }

    eat() {
        this.hunger--;
    }

    drink() {
        this.thirst--;
    }

    play() {
        this.hunger++;
        this.thirst++;
    }
}

class Farm {

    constructor(slot) {
        this.slot = slot;
        this.animals = [];
    }

    breed() {
        if (this.slot > 0) {
            let animal = new Animal();
            this.animals.push(animal);
        } else {
            console.log('Sorry, no more place for any other animal');
        }
    }

    slaughter() {
        this.animals.sort(function(a, b) {
            return b.hunger - a.hunger;
        });
        this.animals.splice(this.animals.length, 1);
    }

    progress() {
        
    }

    farmState() {
        console.log('The farm has ' + this.animals.length + ' living animals, we are bankrupt.');
    }
}