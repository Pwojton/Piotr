function setup() {
  // put setup code here
  createCanvas(700, 600);
}

function draw() {
  // put drawing code here
  fill('#36f20c');
  strokeWeight(10);
  stroke('red');
  ellipse(100, 200, 30, 80);
  stroke('blue');
  fill ('#e00808');
  ellipse(40, 100, 80, 30);

//krzyzyk
  strokeWeight(5);
  stroke('black');
  fill('balck');
  line(10, 10, 60, 60);
  line(60, 10, 10, 60);

  stroke('green');
  fill('green');
  point(100, 100);

  rect(200, 200, 300, 100, 50);
}
