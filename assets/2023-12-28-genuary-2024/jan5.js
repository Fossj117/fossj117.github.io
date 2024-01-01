const jan5 = (s) => {
  let bgcolor = "white";
  let cWidth, cHeight;

  s.setup = () => {
    const myDiv = document.getElementById("jan-5");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    canv = s.createCanvas(cWidth, cHeight);
    s.background(bgcolor);
    s.rectMode(s.CENTER);
    s.noFill();
    s.noLoop();
  };

  s.draw = () => {
    s.background(bgcolor);
    let numRects = Math.floor(s.random(4, 15));
    let minSize = Math.min(cWidth, cHeight);
    let shock = s.random(-minSize / 3, minSize / 3);
    for (let i = 0; i < numRects; i++) {
      s.push();
      s.strokeWeight(s.random(0.5, 2.5));
      s.stroke(
        s.random([
          "#008080", // Teal
          "#6FB98F", // Light Green
          "#A0D6B4", // Mint Green
        ])
      );
      s.rect(
        cWidth / 2 + s.random(-cWidth / 20, cWidth / 20),
        cHeight / 2 + s.random(-cHeight / 20, cHeight / 20),
        minSize / 3 + shock + s.random(-minSize / 10, minSize / 10),
        minSize / 3 + shock + s.random(-minSize / 10, minSize / 10),
        s.random(0, 5)
      );
      s.pop();
    }
  };

  s.mousePressed = () => {
    s.redraw();
  };
};

let jan5sketch = new p5(jan5, "jan-5");
