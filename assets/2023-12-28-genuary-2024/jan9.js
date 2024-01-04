const jan9 = (s) => {
  let ascii_array = [];
  let width;
  let height;
  let fontsize = 10;

  s.setup = () => {
    const myDiv = document.getElementById("jan-9");
    cWidth = myDiv.clientWidth;
    width = Math.floor(cWidth / fontsize);
    height = Math.floor((s.windowHeight * 0.5) / fontsize);
    console.log(width, height);
    s.noCanvas();
    for (let i = 0; i < height; i++) {
      ascii_array.push([]);
      for (let j = 0; j < width; j++) {
        ascii_array[i].push("0");
      }
    }
    s.frameRate(60);
    renderArray();
  };

  function findLeastCommonElement(arr) {
    if (arr.length === 0) {
      return s.random(["0", "."]); // Handle empty array case
    }

    const elementCount = {};
    let leastCommonElement = arr[0];
    let leastCommonCount = 1;

    // Count the occurrences of each element in the array
    for (const element of arr) {
      if (elementCount[element]) {
        elementCount[element]++;
      } else {
        elementCount[element] = 1;
      }

      // Update leastCommonElement and leastCommonCount if needed
      if (elementCount[element] < leastCommonCount) {
        leastCommonElement = element;
        leastCommonCount = elementCount[element];
      }
    }

    return leastCommonElement;
  }

  function renderArray() {
    s.removeElements();
    for (let r = 0; r < ascii_array.length; r++) {
      //   console.log(renderRow(ascii_array[r]));
      let newdiv = s.createDiv(renderRow(ascii_array[r]));
      newdiv.id("num" + r);
    }
  }

  function renderRow(row) {
    res = "";
    for (let e = 0; e < row.length; e++) {
      res += row[e];
    }
    res += "&nbsp;";
    return res;
  }

  function getNeighborVals(x, y) {
    nvals = [];
    let diffvals = [-1, 1, 0];
    for (let a = 0; a < diffvals.length; a++) {
      for (let b = 0; b < diffvals.length; b++) {
        try {
          if (
            ascii_array[x + diffvals[a]][y + diffvals[b]] === undefined ||
            (diffvals[a] == 0 && diffvals[b] == 0)
          ) {
          } else {
            nvals.push(ascii_array[x + diffvals[a]][y + diffvals[b]]);
          }
        } catch {}
      }
    }
    //console.log(nvals);
    return nvals;
  }

  s.draw = () => {
    let randx = s.floor(s.random(0, height));
    let randy = s.floor(s.random(0, width));
    let neighbors = getNeighborVals(randx, randy);
    let updatedVal = "";
    if (neighbors.every((val) => val === neighbors[0])) {
      if (neighbors[0] == "0") {
        updatedVal = ".";
      } else {
        updatedVal = "0";
      }
    } else {
      updatedVal = findLeastCommonElement(neighbors);
    }

    ascii_array[randx][randy] = updatedVal;
    updaterow = s.select("#num" + randx);
    updaterow.html(renderRow(ascii_array[randx]));
  };
};

let jan9sketch = new p5(jan9, "jan-9");
