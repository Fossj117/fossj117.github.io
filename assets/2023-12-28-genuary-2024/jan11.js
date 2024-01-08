const jan11 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;
  let nWide = 10;
  let minWidth;
  let shapeWidth;

  s.setup = () => {
    const myDiv = document.getElementById("jan-11");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    minWidth = Math.min(cWidth, cHeight);
    shapeWidth = Math.floor(minWidth / nWide);
    s.createCanvas(minWidth, minWidth);
    s.noStroke();

    s.background(bgcolor);

    s.noLoop();
  };

  s.draw = () => {
    s.background(bgcolor);
    for (let i = 0; i < nWide; i++) {
      for (let j = 0; j < nWide; j++) {
        elements.push(
          new RectWTri({
            x: shapeWidth / 2 + i * shapeWidth,
            y: shapeWidth / 2 + j * shapeWidth,
            w: shapeWidth,
            h: shapeWidth,
            col1: "beige",
            col2: "teal",
            rot: (s.random([0, 1, 2, 3, 4, 5, 6, 7, 8]) * s.PI) / 2,
          })
        );
      }
    }
    for (let e = 0; e < elements.length; e++) {
      elements[e].draw();
    }
  };

  s.mousePressed = () => {
    s.redraw();
  };

  class RectWTri {
    constructor({ x, y, w, h, col1, col2, rot }) {
      // x and y are the center
      this.x = x;
      this.y = y;
      this.w = w;
      this.h = h;
      this.col1 = col1;
      this.col2 = col2;
      this.rot = rot;

      this.upperleft = { x: -this.w / 2, y: -this.h / 2 };
      this.upperright = { x: +this.w / 2, y: -this.h / 2 };
      this.lowerleft = { x: -this.w / 2, y: +this.h / 2 };
      this.lowerright = { x: +this.w / 2, y: +this.h / 2 };
    }
    update() {}
    draw() {
      s.push();
      s.translate(this.x, this.y);
      s.rotate(this.rot);
      s.fill(this.col1);
      s.triangle(
        this.upperleft.x,
        this.upperleft.y,
        this.upperright.x,
        this.upperright.y,
        this.lowerright.x,
        this.lowerright.y
      );
      s.fill(this.col2);
      s.triangle(
        this.upperleft.x,
        this.upperleft.y,
        this.lowerleft.x,
        this.lowerleft.y,
        this.lowerright.x,
        this.lowerright.y
      );
      s.pop();
    }
  }
};

let jan11sketch = new p5(jan11, "jan-11");
