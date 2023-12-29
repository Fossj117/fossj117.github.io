const jan1 = (sketch) => {
  let num_particles;
  let cx, cy;
  let particles = [];

  sketch.setup = () => {
    let myDiv = document.getElementById("jan-1");
    let cWidth = myDiv.clientWidth;
    let cHeight = sketch.windowHeight * 0.5;
    cx = cWidth / 2;
    cy = cHeight / 2;

    sketch.createCanvas(cWidth, cHeight);
    sketch.background("black");

    num_particles = Math.min(cWidth * 40, 30000);

    for (let i = 0; i < num_particles; i++) {
      let r = sketch.random(0, Math.max(cx, cy) * 1.5);
      particles.push(
        new Particle(
          (r = r),
          (theta = sketch.random(0, 2 * sketch.PI)),
          (vel = sketch.random(0, sketch.PI / (24 * r))),
          (size = sketch.random(0, 3)),
          (color = sketch.random(0, 100))
        )
      );
    }
  };
  sketch.draw = () => {
    sketch.background("black");
    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw();
    }
  };

  class Particle {
    constructor(r, theta, vel, size, color) {
      this.r = r;
      this.theta = theta;
      this.vel = vel;
      this.size = size;
      this.color = color;
    }

    update() {
      this.theta += this.vel;
      this.color += sketch.random(-2, 2);
    }

    draw() {
      sketch.push();
      sketch.translate(cx, cy);
      sketch.translate(
        this.r * sketch.cos(this.theta),
        this.r * sketch.sin(this.theta)
      );
      sketch.fill(255, 255 - this.color / 3, 255 - this.color, 240);
      sketch.noStroke();
      sketch.ellipse(0, 0, this.size);
      sketch.pop();
    }
  }
};

let jan1sketch = new p5(jan1, "jan-1");
