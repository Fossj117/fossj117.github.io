const jan12 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;

  s.setup = () => {
    const myDiv = document.getElementById("jan-12");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    let minSize = Math.min(cWidth, cHeight);
    s.createCanvas(minSize, minSize);
    s.background(bgcolor);
    for (let i = 0; i < 8; i++) {
      elements.push(
        new LavaCircle(
          minSize / 2,
          minSize / 2,
          (i * minSize) / 8,
          100 + s.random(-10, 10)
        )
      );
    }
  };

  let frameCount = 0;

  s.draw = () => {
    frameCount++;
    s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update(frameCount);
      elements[i].draw();
    }
  };

  class LavaCircle {
    constructor(x, y, r, n) {
      this.x = x;
      this.y = y;
      this.r = r;
      this.n = n;
      this.points = [];
      for (let i = 0; i < this.n; i++) {
        this.points.push({
          x: this.x + this.r * s.cos((i * 2 * s.PI) / this.n),
          y: this.y + this.r * s.sin((i * 2 * s.PI) / this.n),
          r: this.r,
        });
      }
      this.val = s.random([-1, 1]);
    }
    update(frame) {
      //update the radius of all the points
      for (let i = 0; i < this.points.length; i++) {
        this.points[i].r =
          this.r + s.sin((this.val * s.cos(i) * frame) / 10) * 10;
        this.points[i].x =
          this.x + this.points[i].r * s.cos((i * 2 * s.PI) / this.n);
        this.points[i].y =
          this.y + this.points[i].r * s.sin((i * 2 * s.PI) / this.n);
      }
    }
    draw() {
      // draw all the points as a shape.
      s.push();
      s.fill(0, 128, 128, 50);
      s.noStroke();
      s.beginShape();
      for (let i = 0; i < this.points.length; i++) {
        s.vertex(this.points[i].x, this.points[i].y);
      }
      s.endShape(s.CLOSE);
      s.pop();
    }
  }
};

let jan12sketch = new p5(jan12, "jan-12");
