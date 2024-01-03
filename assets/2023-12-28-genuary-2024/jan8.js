const jan8 = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;
  let bogMapper;
  let startingPoint;
  let nIters = 10000;
  let currIter = 0;
  let currXY;
  let greenPalette = [
    "#008080", // Teal
    "#6FB98F", // Light Green
    "#A0D6B4", // Mint Green
  ];

  s.setup = () => {
    // Basic setup
    const myDiv = document.getElementById("jan-8");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.createCanvas(cWidth, cHeight);

    eps = s.random([s.random(-3, 3), 0]);
    k = s.random([s.random(-3, 3), 0]);
    mu = s.random([s.random(-2, 2), 0]);
    console.log({ eps: eps, k: k, mu: mu });

    // Start drawing
    s.background(bgcolor);
    bogMapper = new BogMapper({
      epsilon: eps,
      k: k,
      mu: mu,
      maxX: cWidth,
      maxY: cHeight,
    });
    startingPoint = { x: cWidth / 2, y: cHeight / 2 };
    currXY = startingPoint;
    s.fill("black");
    s.frameRate(500);
    s.colorMode(s.RGB);
    s.noStroke();
  };

  s.draw = () => {
    s.fill(0, 128, 128, 100);
    s.ellipse(currXY.x, currXY.y, 4);

    if (currIter < nIters) {
      currXY = bogMapper.map(currXY);
    }
    console.log(currXY);
  };

  class BogMapper {
    // Implements the Bogdanov Map
    //  https://en.wikipedia.org/wiki/Bogdanov_map
    constructor({ epsilon, k, mu, maxX, maxY }) {
      this.epsilon = epsilon;
      this.k = k;
      this.mu = mu;
      this.maxY = maxY;
      this.maxX = maxX;
    }
    map({ x, y }) {
      let y_new =
        (y + this.epsilon * y + this.k * x * (x - 1) + this.mu * x * y) %
        this.maxY;
      let x_new = (x + y_new) % this.maxX;
      return { x: x_new, y: y_new };
    }
  }
};

let jan8sketch = new p5(jan8, "jan-8");
