const jan4 = (s) => {
  let elements = [];
  let bgcolor = 250;
  let cWidth, cHeight;
  let pixelSize = 10;
  let numPixelsWide;
  let numPixelsHigh;
  let pixelLookup = {};
  const colorPalette = [
    "#008080", // Teal
    "#6FB98F", // Light Green
    "#A0D6B4", // Mint Green
    "#8B4513", // Brown
    "#FFA500", // Orange
  ];

  s.setup = () => {
    const myDiv = document.getElementById("jan-4");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.7;

    numPixelsWide = s.floor(cWidth / pixelSize);
    numPixelsHigh = s.floor(cHeight / pixelSize);

    let cnv = s.createCanvas(cWidth, cHeight);
    s.rectMode(s.CENTER);

    //s.background(bgcolor);
    for (let i = 0; i < numPixelsWide; i++) {
      for (let j = 0; j < numPixelsHigh; j++) {
        let nextPix = new Pixel({
          x: (i + 0.5) * pixelSize,
          y: (j + 0.5) * pixelSize,
          w: pixelSize,
          h: pixelSize,
        });
        elements.push(nextPix);
        pixelLookup[pixelXYtoIdx(i, j)] = nextPix;
      }
    }
  };

  s.draw = () => {
    // console.log(s.mouseIsPressed);
    // s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
    if (
      s.mouseX < cWidth &&
      s.mouseX > 0 &&
      s.mouseY > 0 &&
      s.mouseY < cHeight &&
      s.mouseIsPressed
    ) {
      try {
        let curX = s.mouseX + s.random(-20, 20);
        let curY = s.mouseY + s.random(-20, 20);
        mousePix = pixelLookup[canvasXYtoPixelKey(curX, curY)];
        mousePix.state = "SPINNING";
        //console.log(mousePix);
      } catch {}
    }
  };

  function pixelXYtoIdx(pixelX, pixelY) {
    return pixelX.toString() + "," + pixelY.toString();
  }

  function canvasXYtoPixelKey(x, y) {
    // x and y are locations on the canvas
    // returns the lookup key for the pixel
    // corresponding to this canvas location.
    let pixelX = Math.floor(x / pixelSize);
    let pixelY = Math.floor(y / pixelSize);
    return pixelXYtoIdx(pixelX, pixelY);
  }

  class Pixel {
    constructor({ x, y, w, h }) {
      this.x = x;
      this.y = y;
      this.w = w;
      this.h = h;
      this.maxH = h;
      this.spinState = s.PI / 2;
      this.fill = 250;
      this.state = "STATIC";
      this.spinSpeed = 0.1;
    }

    update() {
      if (this.state == "SPINNING") {
        if (this.spinState <= 1 * s.PI + s.PI / 2) {
          this.spinState += this.spinSpeed;
          this.h = s.sin(this.spinState) * this.maxH;
          if (this.h < 0) {
            this.fill = "#009999";
          } else {
            this.fill = 250;
          }
        } else {
          this.state == "STATIC";
        }
      }
    }

    draw() {
      s.push();
      s.noStroke();
      s.fill(this.fill);
      s.rect(this.x, this.y, this.h, this.w);
      s.pop();
    }
  }
};

let jan4sketch = new p5(jan4, "jan-4");
