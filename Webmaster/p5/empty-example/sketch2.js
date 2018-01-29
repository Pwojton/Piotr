var x, y; //współrzędneobiektu
var krok = -1;

function setup() {
  // put setup code here
  createCanvas(600, 600);
  x = 575;
  y = 575;
}

function draw() {
  background(200);
  // put drawing code here
  //r = random(255);
  //g = random(255);
  //b = random(255);

  fill('green');
  strokeWeight(10);
  stroke('blue');
  if (x > 14)
    x = x + krok;
  else {
    x = x - krok;
  }
  if (y> 14){
    y = y + krok;}
    else {
      y = y - krok;
    }
  ellipse(x, y, 30, 30);

}
