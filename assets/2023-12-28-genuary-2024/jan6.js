const jan6 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;
  let greenPalette = [
    "#008080", // Teal
    "#6FB98F", // Light Green
    "#A0D6B4", // Mint Green
  ];

  s.setup = () => {
    const myDiv = document.getElementById("jan-6");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.createCanvas(cWidth, cHeight);

    s.background(bgcolor);
    for (let i = 0; i < 15; i++) {
      elements.push(
        new FlippingCircle(cWidth / 2, cHeight / 2, i * 20 + s.random(-3, 3))
      );
    }
  };

  s.draw = () => {
    s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
  };

  class FlippingCircle {
    constructor(x, y, r) {
      this.x = x;
      this.y = y;
      this.r = r;
      this.currR = r;
      this.currH = r;
      this.numState = 0;
      this.numStateH = 0;
      this.weight = s.random(0.8, 1.8);
      this.rotSpeed = s.random(0.008, 0.015);
      this.rotation = s.random(0, 2 * s.PI);
      this.rotSpeedH = 0; //s.random(0.002, 0.003);
      this.stroke = greenPalette[0]; //s.random(greenPalette);
    }
    setState(x) {
      this.numState = x;
    }
    update() {
      if (this.numState <= 3 * s.PI) {
        this.numState = this.numState + this.rotSpeed;
      }

      //this.numStateH = this.numStateH + this.rotSpeedH;
      this.currR = this.r * s.cos(this.numState);
      this.currH = this.r * s.cos(this.numStateH);
    }
    draw() {
      s.push();
      s.strokeWeight(this.weight);
      s.translate(this.x, this.y);
      s.rotate(this.rotation);
      s.noFill();
      s.stroke(this.stroke);
      s.ellipse(0, 0, this.currH, this.currR);
      s.pop();
    }
  }

  s.mousePressed = () => {
    for (let i = 0; i < elements.length; i++) {
      elements[i].setState(0);
    }
  };
};

let jan6sketch = new p5(jan6, "jan-6");
