class Rectangles {
    constructor(sideA, sideB) {
        this.sideA = sideA;
        this.sideB = sideB;
    }

    getArea() {
        return this.sideA * this.sideB;
    }

    getCircumference() {
        return 2 * this.sideA + 2 * this.sideB;
    }
}

const rectangle = new Rectangles(10, 4);

console.log(rectangle.getArea());
console.log(rectangle.getCircumference())
