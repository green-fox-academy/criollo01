function Sharpie (color, width, inkAmount) {
    this.color = color;
    this.width = width;
    this.inkAmount = 100;
    this.use = function() {
        this.inkAmount -= this.width;
        if (this.inkAmount < 0) {
            this.inkAmount = 0;
        }
    }
}

let newSharpie = new Sharpie ('green', 40);
while (newSharpie.inkAmount > 0) {
    newSharpie.use();
    console.log(newSharpie.inkAmount);
}