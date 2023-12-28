let num_particles;
let cx, cy;
let particles = [];

function setup() {
  let cWidth = windowWidth * 0.5;
  let cHeight = windowHeight * 0.5;
  cx = cWidth / 2;
  cy = cHeight / 2;

  const canvas = createCanvas(cWidth, cHeight);
  canvas.parent("jan-1");
  background("black");

  num_particles = Math.min(cWidth * 40, 30000);

  for (let i = 0; i < num_particles; i++) {
    let r = random(0, Math.max(cx, cy) * 1.5);
    particles.push(
      new Particle(
        (r = r),
        (theta = random(0, 2 * PI)),
        (vel = random(0, PI / (24 * r))),
        (size = random(0, 3)),
        (color = random(0, 100))
      )
    );
  }
}
function draw() {
  background("black");
  for (let i = 0; i < particles.length; i++) {
    particles[i].update();
    particles[i].draw();
  }
}

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
    this.color += random(-2, 2);
  }

  draw() {
    push();
    translate(cx, cy);
    translate(this.r * cos(this.theta), this.r * sin(this.theta));
    fill(255, 255 - this.color / 3, 255 - this.color, 240);
    noStroke();
    ellipse(0, 0, this.size);
    pop();
  }
}
