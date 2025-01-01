const jan2 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;

  s.setup = () => {
    const myDiv = document.getElementById("jan-2");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.createCanvas(cWidth, cHeight);

    s.background(bgcolor);
    for (let i = 0; i < 1000; i++) {
      let x = s.random(cWidth);
      let y = s.random(cHeight);
      let radius = s.random(20, 100);
      let vertices = s.floor(s.random(3, 10));
      let angleOffsetSpeed = s.random(0.0005, 0.01);
      elements.push(new Shape(x, y, radius, vertices, angleOffsetSpeed));
    }
  };

  s.draw = () => {
    s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
  };

  class Shape {
    constructor(x, y, radius, vertices, angleOffsetSpeed) {
      this.x = x;
      this.y = y;
      this.radius = radius;
      this.vertices = vertices;
      this.angleOffset = 0;
      this.angleOffsetSpeed = angleOffsetSpeed;
    }

    update() {
      // Incrementally change the angle offset for smooth vertex shifting
      this.angleOffset += this.angleOffsetSpeed;

      // Gradually drift the x and y positions
      this.x += s.random(-0.5, 0.5);
      this.y += s.random(-0.5, 0.5);

      // Wrap around the canvas
      if (this.x < 0) this.x = cWidth;
      if (this.x > cWidth) this.x = 0;
      if (this.y < 0) this.y = cHeight;
      if (this.y > cHeight) this.y = 0;

      // Gradually change the radius
      this.radius += s.random(-0.2, 0.2);
    }

    draw() {
      s.push();
      s.fill(100, 150, 200, 5); // Example fill color with lowest possible alpha
      s.noStroke();
      s.beginShape();
      for (let i = 0; i < this.vertices; i++) {
        let angle = s.TWO_PI / this.vertices * i + this.angleOffset;
        let x = this.x + this.radius * s.cos(angle);
        let y = this.y + this.radius * s.sin(angle);
        s.vertex(x, y);
      }
      s.endShape(s.CLOSE);
      s.pop();
    }
  }
};

let janXsketch = new p5(jan2, "jan-2");
