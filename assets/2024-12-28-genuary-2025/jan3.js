const jan3 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth 
  let cHeight;
  s.setup = () => {
    const myDiv = document.getElementById("jan-3");
    cWidth = myDiv.clientWidth; cHeight = s.windowHeight * 0.5; s.createCanvas(cWidth, cHeight);
    s.rectMode(s.CENTER);
    s.background(bgcolor);
    const N = 200; // Define the number of elements you want to add
    for (let i = 0; i < N; i++) {
      elements.push(new Element());
    }
  };
  s.draw = () => {
    s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
  };
  class Element {
    constructor() {
      this.x = Math.random() * cWidth; this.y = Math.random() * cHeight;
      this.size = Math.random() * 50 + 50; // Initial size between 10 and 60
      this.growthRate = Math.random() * 0.04 + 0.2; // Growth rate between 0.1 and 0.6
      this.maxSize = cWidth * 2; // Max size
      this.growing = true; // Always growing
      this.alpha = Math.random() * 80; // Semi-transparent with random low alpha value
    }
    update() {
      if (this.size < this.maxSize) { this.size += this.growthRate;}
    }
    draw() {
      s.push();
      s.fill(100, 100, 250, this.alpha);s.noStroke(); s.textAlign(s.CENTER, s.CENTER); s.textSize(this.size); s.text("42", this.x, this.y); // Draw the text "42"
      s.pop();
    }
  }
};
let jan3sketch = new p5(jan3, "jan-3");
