const janX = (s) => {
  let elements = [];
  let bgcolor = "white";
  let cWidth, cHeight;

  s.setup = () => {
    const myDiv = document.getElementById("jan-X");
    cWidth = myDiv.clientWidth;
    cHeight = s.windowHeight * 0.5;
    s.createCanvas(cWidth, cHeight);

    s.background(bgcolor);
    elements.push(new Element());
  };

  s.draw = () => {
    s.background(bgcolor);
    for (let i = 0; i < elements.length; i++) {
      elements[i].update();
      elements[i].draw();
    }
  };

  class Element {
    constructor() {}
    update() {}
    draw() {}
  }
};

let janXsketch = new p5(janX, "jan-X");
