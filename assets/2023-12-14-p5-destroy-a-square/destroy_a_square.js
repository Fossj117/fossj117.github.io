let blocks = [];
let numSquaresSide = 25;
let size = 5;
let xoffset = 200;
let yoffset = 0;
let ground;
let counter = 0;
let engine;

function setup() {
  const canvas = createCanvas(500, 500);
  canvas.parent("sketch-holder");

  // create an engine
  engine = Matter.Engine.create();
  let world = engine.world;
  world.gravity.y = 0.4;

  for (let x = 0; x < numSquaresSide; x++) {
    for (let y = 0; y < numSquaresSide; y++) {
      blocks.push(
        new Block(
          world,
          {
            x: xoffset + x * size,
            y: yoffset + y * size,
            w: size,
            h: size,
            color: "#2a7ae2",
          },
          { restitution: 0.5, friction: 0.1 }
        )
      );
    }
  }

  breaker = new Block(
    world,
    { x: 265, y: 360, w: 100, h: 15, color: "black" },
    { isStatic: true, angle: PI / 7 }
  );
  ground = new Block(
    world,
    { x: 0, y: 500, w: 1000, h: 20, color: "black" },
    { isStatic: true }
  );
  wallRight = new Block(
    world,
    { x: 500, y: 500, w: 1000, h: 20, color: "black" },
    { isStatic: true, angle: PI / 2 }
  );
  wallLeft = new Block(
    world,
    { x: 0, y: 0, w: 1000, h: 20, color: "black" },
    { isStatic: true, angle: PI / 2 }
  );

  // run the engine
  Matter.Runner.run(engine);
}

function draw() {
  background("white");
  blocks.forEach((x) => x.draw());
  breaker.draw();
  ground.draw();
  wallRight.draw();
  wallLeft.draw();
  counter = counter + 1;
  // console.log(counter);
  if (counter > 2000) {
    noLoop();
  }
}

/*
This class allows the block
- to drawn with various attributes
- to be placed as a rectangle in the world as a physical Matter body
*/
class BlockCore {
  // attrs: visual properties of the block e.g. position and dimensions
  // options: definies the behaviour of the block e.g. mass and bouncyness
  constructor(world, attrs, options) {
    this.world = world;
    this.attrs = attrs;
    this.options = options || {};
    this.options.plugin = this.options.plugin || {};
    this.options.plugin.block = this;
    this.addBody();
    if (this.body) {
      Matter.World.add(this.world, this.body);
      if (this.options.restitution) {
        this.body.restitution = this.options.restitution;
      }
    }
  }

  addBody() {
    this.body = Matter.Bodies.rectangle(
      this.attrs.x,
      this.attrs.y,
      this.attrs.w,
      this.attrs.h,
      this.options
    );
  }

  draw() {
    if (this.body) {
      if (this.attrs.color) {
        fill(this.attrs.color);
      } else {
        noFill();
      }
      noStroke();
      this.drawBody();
    }
  }

  drawBody() {
    if (this.body.parts && this.body.parts.length > 1) {
      // skip index 0
      for (let p = 1; p < this.body.parts.length; p++) {
        this.drawVertices(this.body.parts[p].vertices);
      }
    } else {
      if (this.body.type == "composite") {
        for (let body of this.body.bodies) {
          this.drawVertices(body.vertices);
        }
      } else {
        this.drawVertices(this.body.vertices);
      }
    }
  }

  drawVertices(vertices) {
    beginShape();
    for (const vertice of vertices) {
      vertex(vertice.x, vertice.y);
    }
    endShape(CLOSE);
  }
}

class Block extends BlockCore {
  constructor(world, attrs, options) {
    super(world, attrs, options);
    this.collisions = [];
    this.constraints = [];
  }

  draw() {
    this.update();
    super.draw();
    if (this.constraints.length > 0) {
      for (let c of this.constraints) {
        if (c.draw === true) this.drawConstraint(c);
      }
    }
  }

  drawConstraints() {
    if (this.constraints.length > 0) {
      for (let c of this.constraints) {
        this.drawConstraint(c);
      }
    }
  }

  drawConstraint(constraint) {
    stroke("magenta");
    strokeWeight(2);
    const offsetA = constraint.pointA;
    let posA = {
      x: 0,
      y: 0,
    };
    if (constraint.bodyA) {
      posA = constraint.bodyA.position;
    }
    const offsetB = constraint.pointB;
    let posB = {
      x: 0,
      y: 0,
    };
    if (constraint.bodyB) {
      posB = constraint.bodyB.position;
    }
    line(
      posA.x + offsetA.x,
      posA.y + offsetA.y,
      posB.x + offsetB.x,
      posB.y + offsetB.y
    );
  }

  update() {
    this.collisions.forEach((block) => {
      if (block.attrs.force) {
        Matter.Body.applyForce(
          this.body,
          this.body.position,
          block.attrs.force
        );
      }
      if (block.attrs.trigger) {
        block.attrs.trigger(this, block);
      }
    });
    this.collisions = [];

    if (this.attrs.chgStatic) {
      Matter.Body.setStatic(this.body, false);
    }

    if (this.attrs.rotate) {
      // set angle of propeller
      Matter.Body.setAngle(this.body, this.attrs.rotate.angle);
      Matter.Body.setAngularVelocity(this.body, 0.15);
      // increase angle
      this.attrs.rotate.angle += this.attrs.rotate.delta;
    }
  }

  constrainTo(block, options) {
    options.bodyA = this.body;
    if (block) {
      // constrain to another block
      if (!options.bodyB) {
        options.bodyB = block.body;
      }
    } else {
      // constrain to "background" scene
      if (!options.pointB) {
        options.pointB = { x: this.body.position.x, y: this.body.position.y };
      }
    }
    const contraint = Matter.Constraint.create(options);
    this.constraints.push(contraint);
    Matter.World.add(this.world, contraint);
    return contraint;
  }

  collideWith(block) {
    if (block) {
      this.collisions.push(block);
    }
  }
}
