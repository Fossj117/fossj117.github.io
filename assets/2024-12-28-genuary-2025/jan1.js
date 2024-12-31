  // Start of Selection
const jan1 = (sketch) => {
    let cx, cy;
    let particles; 
    let lines;
    const colorPalette = [
        // "#008080", // Teal
        "#6FB98F", // Light Green
        // "#A0D6B4", // Mint Green
        // "#8B4513", // Brown
        // "#FFA500", // Orange
    ];

    sketch.setup = () => {
      let myDiv = document.getElementById("jan-1");
      let cWidth = myDiv.clientWidth;
      let cHeight = sketch.windowHeight * 0.5;
      cx = cWidth / 2;
      cy = cHeight / 2;

      sketch.createCanvas(cWidth, cHeight);
      sketch.background("white");
      particles = [];
      lines = [];

      particles.push(new Particle());
      // particles.push(new Particle());
    };

    sketch.draw = () => {
      sketch.background(255, 255, 255, 25);

      for (let particle of particles) {
        particle.update();
        // particle.draw();

        // Create a new line based on particle location
        let numLines = Math.floor(Math.random() * 20) + 1; // Random number between 1 and 10
        for (let j = 0; j < numLines; j++) {
          let isVertical = Math.random() < 0.5;
          let line = new Line(isVertical, Math.floor(Math.random() * 200) + 30); // Random age between 50 and 250

          if (isVertical) {
            line.x = particle.x + sketch.randomGaussian() * 25; // Adjust 10 to control the spread
          } else {
            line.y = particle.y + sketch.randomGaussian() * 25; // Adjust 10 to control the spread
          }

          lines.push(line);
        }
      }

      for (let i = lines.length - 1; i >= 0; i--) {
        let l = lines[i];
        
        l.update();
        l.draw();

        // Remove the line if its age is 0
        if (l.age <= 0) {
          lines.splice(i, 1);
        }
      }
    };

    class Line {
      constructor(isVertical, age) {
        this.isVertical = isVertical;
        this.age = age;
        this.maxAge = age;
        this.color = sketch.random(colorPalette);
        if (this.isVertical) {
          this.x = Math.random() * sketch.width;
          this.y1 = 0;
          this.y2 = sketch.height;
        } else {
          this.y = Math.random() * sketch.height;
          this.x1 = 0;
          this.x2 = sketch.width;
        }
      }

      update() {
        this.age--;
      }

      draw() {
        sketch.push(); // Save the current drawing style settings
        let alpha = sketch.map(this.age, 0, this.maxAge, 0, 25);
        let lineColor = sketch.color(this.color);
        lineColor.setAlpha(alpha);
        sketch.stroke(lineColor);
        sketch.strokeWeight(2);
        if (this.isVertical) {
            sketch.line(this.x, this.y1, this.x, this.y2);
        } else {
          sketch.line(this.x1, this.y, this.x2, this.y);
        }
        sketch.pop(); // Restore the previous drawing style settings
      }
    }

    class Particle {
      constructor() {
        this.x = Math.random() * sketch.width;
        this.y = Math.random() * sketch.height;
        this.xOffset = Math.random() * 1000;
        this.yOffset = Math.random() * 1000;
      }

      update() {
        // Use Perlin noise for smooth and organic motion
        this.x += sketch.map(sketch.noise(this.xOffset), 0, 1, -3.5, 3.5); // Increase range for more drift
        this.y += sketch.map(sketch.noise(this.yOffset), 0, 1, -3.5, 3.5); // Increase range for more drift
        
        this.xOffset += 0.01;
        this.yOffset += 0.01;

        // Wrap the particle around the edges of the canvas
        if (this.x < 0) this.x = sketch.width;
        if (this.x > sketch.width) this.x = 0;
        if (this.y < 0) this.y = sketch.height;
        if (this.y > sketch.height) this.y = 0;
      }

      draw() {
        sketch.fill(255);
        sketch.noStroke();
        sketch.ellipse(this.x, this.y, 5, 5);
      }
    }
};

let jan1sketch = new p5(jan1, "jan-1");