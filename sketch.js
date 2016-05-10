var x = 0;
var y = 0;
var scl = 300;

function setup() {
  createCanvas(500, 500);
}

function draw() {
  background(0);
  stroke(255);
  fill(255);
  ellipse(width/2, height/2, sin(x)*scl, cos(y)*scl)
  x += 0.05;
  y += 0.05;
}