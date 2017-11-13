function Rectangles (sideA, sideB) {
    this.sideA = sideA;
    this.sideB = sideB;
}

Rectangles.prototype.getArea = function (){
    return this.sideA * this.sideB;
}

Rectangles.prototype.getCircumference = function() {
    return 2 * (this.sideA + this.sideB);
}

const rect = new Rectangles(4, 5)
console.log(rect.getArea());
console.log(rect.getCircumference());