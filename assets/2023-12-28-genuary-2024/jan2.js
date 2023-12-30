const jan2 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;

  let NUMFLOWERS = 200;
  let maxElements = 5000;

  s.setup = () => {
    const myDiv = document.getElementById("jan-2");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.colorMode(s.HSB, 100);
    var canvas = s.createCanvas(cWidth, cHeight);
    canvas.mouseClicked(s.refresh);
    s.makeFlowers();
  };

  s.draw = () => {
    s.background(bgcolor);

    // Update and render everyhting
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }

    // Remove dead flowers
    elements = elements.filter((x) => x.state != "DEAD");

    // Stop
    if (elements.length > maxElements) {
      for (let i = 0; i < elements.length; i++) {
        elements[i].state = "DYING";
      }
    } else if (elements.length == 0) {
      s.refresh();
    }
  };

  s.refresh = () => {
    elements = [];
    s.makeFlowers();
  };

  s.clamp = (value) => Math.min(95, Math.max(5, value));

  s.funExplore = (value) => {
    if (s.random() < 0.05) {
      return s.random(-20, 20);
    } else {
      return s.random(-5, 5);
    }
  };

  s.makeFlowers = () => {
    let baseHue = s.random(0, 100);
    for (let i = 0; i < NUMFLOWERS; i++) {
      elements.push(
        new Flower({
          x: s.random(0, cWidth),
          y: s.random(0, cHeight),
          r: s.random(0, 10),
          hue: baseHue,
          sat: s.clamp(90 + s.random(-20, 20)),
          bright: 90 + s.random(-10, 10),
          alpha: 90 + s.random(-10, 10),
          growthrate: s.random(0.35, 0.9),
          lifetime: s.random(20, 100),
          state: "GROWING",
        })
      );
    }
  };

  class Element {
    constructor() {}
    update() {}
    draw() {}
  }

  class Flower extends Element {
    static states = ["DYING", "GROWING", "DEAD"];

    constructor({
      x,
      y,
      r,
      hue,
      sat,
      bright,
      alpha,
      growthrate,
      lifetime,
      state,
    }) {
      super();
      this.x = x;
      this.y = y;
      this.r = r;
      this.growthrate = growthrate;
      this.hue = hue;
      this.sat = sat;
      this.bright = bright;
      this.alpha = alpha;
      this.age = 0;
      this.lifetime = lifetime;
      this.state = state;
    }
    update() {
      if (this.state == "GROWING") {
        this.age += 1;
        this.r += this.growthrate;
        if (this.age >= this.lifetime) {
          // you're dead!
          this.state = "DYING";
          if (s.random() > 0.2) {
            let numOffspring = s.random(0, 3);
            for (let i = 0; i < numOffspring; i++) {
              elements.push(
                new Flower({
                  x: this.x + s.random(-20, 20),
                  y: this.y + s.random(-20, 20),
                  r: this.r / 20,
                  hue: s.clamp(this.hue + s.funExplore()),
                  sat: s.clamp(this.sat + s.random(-5, 5)),
                  bright: s.clamp(this.bright + s.random(-5, 5)),
                  alpha: s.clamp(this.alpha + s.random(-5, 5)),
                  growthrate: this.growthrate,
                  lifetime: s.random(20, 100),
                  state: "GROWING",
                })
              );
            }
          }
        }
      } else if (this.state == "DYING") {
        if (this.alpha > 0) {
          this.alpha = this.alpha - 1;
        } else {
          this.alpha = 0;
          this.state = "DEAD";
        }
      }
    }
    draw() {
      if (this.state != "DEAD") {
        s.push();
        s.translate(this.x, this.y);
        s.noStroke();
        s.fill(this.hue, this.sat, this.bright, this.alpha);
        s.ellipse(0, 0, this.r);
        s.pop();
      }
    }
  }
};

let jan2sketch = new p5(jan2, "jan-2");
