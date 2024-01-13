const jan13 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;
  let cX, cY;
  let tealColor;

  s.setup = () => {
    const myDiv = document.getElementById("jan-13");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    minVal = Math.min(cWidth, cHeight);
    s.createCanvas(minVal, minVal);
    cX = minVal / 2;
    cY = minVal / 2;
    canv = s.background(bgcolor);
    for (let i = 0; i < 400; i++) {
      elements.push(
        new Dot({
          r: 100,
          theta: 0,
          a: s.random(0.1, 4),
          b: s.random(0.1, 4),
          rate: 0.01,
        })
      );
    }
    s.noStroke();
    tealColor = s.color(0, 128, 128, 225);
  };

  s.draw = () => {
    s.background(bgcolor);
    s.push();
    s.translate(cX, cY);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
    s.pop();
  };

  class Dot {
    constructor({ r, theta, a, b, rate }) {
      this.r = r;
      this.theta = theta;
      this.a = a;
      this.b = b;
      this.rate = rate; //0.01
    }
    update() {
      this.theta += this.rate;
    }
    draw() {
      s.push();
      s.fill(tealColor);
      s.translate(
        this.r * this.wobblyCos(this.theta),
        this.r * this.wobblySin(this.theta)
      );
      s.ellipse(0, 0, 8, 8);
      s.pop();
    }
    wobblyCos(x) {
      return s.cos(this.a + this.b * s.cos(x));
    }
    wobblySin(x) {
      return s.sin(this.a + this.b * s.sin(x));
    }
  }
};

let jan13sketch = new p5(jan13, "jan-13");
