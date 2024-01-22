const jan16 = (s) => {
  let elements = [];
  let bgcolor = "white";
  //   let myColor = "teal";
  // light teal color with alpha
  let myColor = s.color(0, 128, 128, 75);
  let cWidth, cHeight;
  let numElts = 10000;

  s.setup = () => {
    const myDiv = document.getElementById("jan-16");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.createCanvas(cWidth, cHeight);

    s.background(bgcolor);
    for (let i = 0; i < numElts; i++) {
      elements.push(new Element({ x: s.random(cWidth), y: s.random(cHeight) }));
    }
    console.log(elements);
  };

  s.draw = () => {
    s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      // randomly double update for some elements if they are in a band
      if (s.random() < s.sin(s.frameCount * 0.01)) {
        elements[i].update();
      }
      elements[i].draw();
    }
  };

  class Element {
    constructor({ x, y }) {
      this.x = x;
      this.y = y;
      this.points = [];
      this.r = s.random(2, 10);
      this.rotspeed = s.random(0.001, 0.03);
      this.currTheta = 0;
      this.currScale = 1;
      // Add points in a circle
      for (let i = 0; i < 1; i++) {
        let theta = s.map(i, 0, 10, 0, s.TWO_PI);
        let x = this.r * s.cos(theta);
        let y = this.r * s.sin(theta);
        this.points.push({ x: x, y: y });
      }
    }
    update() {
      // rotate the whole shape
      this.currTheta += this.rotspeed;
      this.currScale = s.map(s.cos(this.currTheta), -1, 1, 0.5, 3);
      // drift the shape
      this.x += s.random(-0.1, 0.1);
      this.y += s.random(-0.1, 0.1);
    }
    draw() {
      s.push();
      s.translate(this.x, this.y);
      s.rotate(this.currTheta);
      s.scale(this.currScale);
      s.noStroke();
      s.fill(myColor);
      s.strokeWeight(0.1);
      for (let i = 0; i < this.points.length; i++) {
        // draw the points as a circle
        s.ellipse(this.points[i].x, this.points[i].y, 2, 2);
      }
      s.pop();
    }
  }
};

let jan16sketch = new p5(jan16, "jan-16");
