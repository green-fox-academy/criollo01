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
        this.animals.length < this.slots) {
            this.animals.push(new Animal());
        }
    }
    slaughter() {
        animalHunger = [];
        this.animals.forEach(function(e)) {
            animalHunger.push(e.hunger);
        });
        this.animals.splice(animalHunger.indexOf(Math.min(...animalHunger)), 1);
        this.slots++;
    }

    progress() {

    }

    farmState() {
        let stateOfFarm = '';
        if (this.animals.length === 0) {
            stateOfFarm = 'bankrupt';
        } else if (this.animals.length < this.slot) {
            stateOfFarm = 'okay';
        } else {
            stateOfFarm = 'full';
        }
        console.log('The farm has ' + this.animals.length + ' living animals, we are ' + stateOfFarm.');
    }