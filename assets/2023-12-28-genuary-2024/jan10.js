const jan10 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;
  let hexVertices;
  let currRadius;
  let num_particles = 2000;
  let greenPalette = [
    "#008080", // Teal
    "#6FB98F", // Light Green
    "#A0D6B4", // Mint Green
  ];
  let frameCount = 0;

  s.setup = () => {
    const myDiv = document.getElementById("jan-10");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.createCanvas(cWidth, cHeight);
    s.background(bgcolor);

    currRadius = Math.min(cWidth, cHeight) * 0.75 * 0.5;
    hexVertices = getHexagonCorners({
      radius: currRadius,
      xoffset: cWidth / 2,
      yoffset: cHeight / 2,
    });
    console.log(hexVertices);
    for (const v of hexVertices) {
      s.push();
      s.fill("black");
      s.ellipse(v.x, v.y, 10, 10);
      s.pop();
    }

    for (let i = 0; i < num_particles; i++) {
      elements.push(
        new Particle({
          x: s.random(0, cWidth),
          y: s.random(0, cHeight),
          targets: hexVertices,
          color: s.random(greenPalette),
        })
      );
    }
  };

  s.draw = () => {
    frameCount += 1;
    s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
  };

  function getHexagonCorners({ radius, xoffset, yoffset }) {
    //from chatgpt
    let corners = [];
    for (let i = 0; i < 6; i++) {
      // Angle in radians
      let angle = (Math.PI / 3) * i;
      let x = radius * Math.cos(angle);
      let y = radius * Math.sin(angle);
      corners.push({ x: x + xoffset, y: y + yoffset });
    }
    return corners;
  }

  // just standard distance function
  function distance(x1, y1, x2, y2) {
    return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
  }

  function normalizeVector({ x, y }) {
    // Calculate the magnitude of the vector
    let magnitude = Math.sqrt(x * x + y * y);

    // Check if the magnitude is zero to avoid division by zero
    if (magnitude === 0) {
      return { x: 0, y: 0 };
    }

    // Divide each component by the magnitude to get the normalized vector
    let normalizedX = x / magnitude;
    let normalizedY = y / magnitude;

    return { x: normalizedX, y: normalizedY };
  }

  class Particle {
    constructor({ x, y, targets }) {
      this.pos = { x: x, y: y };
      this.targets = targets;
      this.color = s.random(greenPalette);
      this.speed = s.random(0.5, 3);
      this.updateTarget();
    }
    update() {
      if (distance(this.pos.x, this.pos.y, this.target.x, this.target.y) < 10) {
        this.target = s.random(this.targets);
        this.updateTarget();
      } else {
        this.pos.x += this.direction.x * this.speed;
        this.pos.y += this.direction.y * this.speed;
      }
    }
    draw() {
      s.push();
      s.noStroke();
      s.fill(this.color);
      s.ellipse(this.pos.x, this.pos.y, 5, 5);
      s.pop();
    }
    updateTarget() {
      if (
        s.random() <
        Math.sin((frameCount / 120) * (s.PI / 12)) *
          Math.sin((frameCount / 120) * (s.PI / 12))
      ) {
        this.target = { x: s.random(0, cWidth), y: s.random(0, cHeight) };
        this.speed = s.random(0.5, 1.4);
      } else {
        this.target = s.random(this.targets);
        this.speed = s.random(1.5, 5);
      }
      this.direction = normalizeVector({
        x: this.target.x - this.pos.x + s.random(-5, 5),
        y: this.target.y - this.pos.y + s.random(-5, 5),
      });
    }
  }
};

let jan10sketch = new p5(jan10, "jan-10");
