const jan3 = (s) => {
  let elements = [];
  let bgHue = 55;
  let cWidth, cHeight;
  let scaleFactor = 0.995; // how much to scale down size on each recurse

  s.setup = () => {
    const myDiv = document.getElementById("jan-1");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.colorMode(s.HSB, 100);
    s.createCanvas(cWidth, cHeight);
    // s.background(bgHue, 100, 100, 100);
    elements.push(
      new RecursiveBouncingRect({
        x: s.random(0, cWidth - cWidth * scaleFactor),
        y: s.random(0, cHeight - cHeight * scaleFactor),
        width: cWidth * scaleFactor,
        height: cHeight * scaleFactor,
        xSpeed: s.random(0.0005, 0.008),
        ySpeed: s.random(0.0005, 0.008),
        xMax: cWidth,
        yMax: cHeight,
        fill: 100,
      })
    );
  };

  s.draw = () => {
    // s.background(bgHue, 100, 100, 100);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
  };

  class Element {
    constructor() {}
    update() {}
    draw() {}
  }

  class RecursiveBouncingRect extends Element {
    constructor({ x, y, width, height, xSpeed, ySpeed, xMax, yMax, fill }) {
      super();
      this.x = x;
      this.y = y;
      this.width = width;
      this.height = height;
      this.xSpeed = xSpeed;
      this.ySpeed = ySpeed;
      this.xMax = xMax;
      this.yMax = yMax;
      this.fill = fill;
      this.hasChild = false;

      if (this.width < 20 || this.height < 20) {
        // no recurse, base case
      } else {
        this.hasChild = true;
        this.child = new RecursiveBouncingRect({
          x: this.x * scaleFactor,
          y: this.y * scaleFactor,
          width: this.width * scaleFactor,
          height: this.height * scaleFactor,
          xSpeed: this.xSpeed * scaleFactor,
          ySpeed: this.ySpeed * scaleFactor,
          xMax: this.xMax * scaleFactor,
          yMax: this.yMax * scaleFactor,
          fill: this.fill * scaleFactor,
        });
      }
    }

    update() {
      this.x += this.xSpeed;
      this.y += this.ySpeed;
      if (this.x <= 0 || this.x + this.width >= this.xMax) {
        this.xSpeed *= -1;
      }
      if (this.y <= 0 || this.y + this.height >= this.yMax) {
        this.ySpeed *= -1;
      }
      if (this.hasChild) {
        this.child.update();
      }
    }

    draw() {
      s.push();
      s.noStroke();
      s.fill(
        s.map(this.fill, 0, 100, 35, 50),
        s.map(this.fill, 0, 100, 0, 80),
        s.map(100 - this.fill, 0, 100, 50, 100),
        100
      );
      s.translate(this.x, this.y);
      s.rect(0, 0, this.width, this.height);
      if (this.hasChild) {
        this.child.draw();
      }
      s.pop();
    }
  }
};

let jan3sketch = new p5(jan3, "jan-3");
