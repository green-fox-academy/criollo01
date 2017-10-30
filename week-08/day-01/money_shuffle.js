const Shuffler = {
    dollars : 10000,
    pick: function (){
        if (Panama.cash > Cyprus.cash) {
            Cyprus.deposit(1000);
        } else {
            Panama.deposit(1000);
        }
    }
}

const Panama = {
    name : 'Panama',
    tax : '1%',
    cash : 0,
    deposit: function (amount) {
        this.cash += amount;
        console.log('Panama got ' + amount);
    }
}

const Cyprus = {
    name : 'Cyprus',
    tax : '5%',
    cash : 0,
    deposit: function (amount) {
        this.cash += amount;
        console.log('Cyprus got ' + amount);
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000