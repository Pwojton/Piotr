
function setup() {
  // put setup code here
  createCanvas(600, 600);

}

function draw() {
    background(200);
    dx = mouseX - x;
    dy = mouseY - y;
    angle1 = atan2(dx, dy);
    x = mouseX - (cos(angel1) * 30);
    y = mouseY - (sin(angle1) * 30);
  rect(x, y, 30, 30);

}
