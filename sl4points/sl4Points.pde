float xmag, ymag = 0;
float newXmag, newYmag = 0;
float r = 500;
float ex = 70;
float phi;
float theta;
float[][] result;
float g = 10;
float step = 5;
float scl = 530;

PVector v1, v2, v4, v5;

void setup() {
  size(800, 700, P3D);

  String[] output = loadStrings("output3.txt");  //change to "output", "output2", "output3" to see the first, second and third symmetric powers

  result = new float[output.length][1];

  for (int i = 0; i < output.length; i++) {
    output[i] = output[i].substring(1, output[i].length()-2);
    float[] data = float(split(output[i], ", "));
    result[i] = data;

    v1 = new PVector(-9, -1, -13);
    v2 = new PVector(-5, -1, -9);
    v4 = new PVector(-1, 0, -2);
    v5 = new PVector(-1, 0, -1.5);  //these vectors surround a quadrilateral region


    v1.normalize();
    v2.normalize();
    v4.normalize();
    v5.normalize();

    v1.mult(scl);
    v2.mult(scl);
    v4.mult(scl);
    v5.mult(scl);
  }
}

void draw() {
  background(#CEEDFF);

  pushMatrix();
  translate(width/2, height/2, -r);

  newXmag = mouseX/float(width) * TWO_PI;
  newYmag = mouseY/float(height) * TWO_PI;

  float diff = xmag-newXmag;
  if (abs(diff) >  0.01) {
    xmag -= diff/4.0;
  }

  diff = ymag-newYmag;
  if (abs(diff) >  0.01) {
    ymag -= diff/4.0;
  }

  rotateX(-ymag);
  rotateY(-xmag);

  strokeWeight(1);
  for (int i = 0; i < result.length; i++) {
    for (int j = 0; j < result[i].length; j++) {
      phi = i*180/result.length;
      theta = result[i][j];
      pushMatrix();
      rotateZ(radians(theta));
      rotateY(radians(phi));
      translate(0, 0, r);
      strokeWeight(1.5);
      stroke(0, 0, 0);
      fill(0, 0, 0);
      point(0, 0);
      popMatrix();
    }
  }

  colorMode(RGB, 255, 255, 255, 100);
  noStroke();
  fill(255);
  sphere(r);
  basis();

  strokeWeight(5);
  stroke(255, 0, 255);
  line(0, 0, 0, v1.x, v1.y, v1.z);
  line(0, 0, 0, v2.x, v2.y, v2.z);
  line(0, 0, 0, v4.x, v4.y, v4.z);
  line(0, 0, 0, v5.x, v5.y, v5.z);


  pushMatrix();
  rotateZ(radians(170));
  rotateY(radians(25));
  translate(0, 0, r+1);
  noStroke();
  fill(#FF8F05); //orange
  //ellipse(0, 0, 13, 13);    //use Sketch > Tweak to move these circles around on the surface of the sphere
  popMatrix();

  pushMatrix();
  rotateZ(radians(286));
  rotateY(radians(157));
  translate(0, 0, r+1);
  noStroke();
  fill(#19CB23); //green
  //ellipse(0, 0, 13, 13);    //use 'Sketch > Tweak' to move these circles around on the surface of the sphere
  popMatrix();

  popMatrix();

  if (keyPressed == true) {
    save("image.png");
    println("image saved");
  }
}

void basis() {    //draws co-ordinate axis
  strokeWeight(2);
  stroke(255, 0, 0); // x-axis
  fill(255, 0, 0);
  line(-(r+ex), 0, (r+ex), 0);
  ellipse((r+ex), 0, g, g);
  stroke(0, 255, 0);  // y-axis
  fill(0, 255, 0);
  line(0, -(r+ex), 0, (r+ex));
  ellipse(0, (r+ex), g, g);
  pushMatrix();
  rotateY(PI/2);
  stroke(0, 0, 255);  // z-axis
  fill(0, 0, 255);
  line(-(r+ex), 0, (r+ex), 0);
  ellipse(-(r+ex), 0, g, g);
  popMatrix();


  //strokeWeight(0.5);    //uncomment these two blocks to add gridlines
  //for (float i = 0; i < 180; i+= step) {
  //  pushMatrix();
  //  rotateX(PI/2);
  //  pushMatrix();
  //  rotateY(radians(i));
  //  stroke(0, 50);
  //  noFill();
  //  ellipse(0, 0, 2*r, 2*r);
  //  popMatrix();
  //  popMatrix();
  //}

  //for (float j = 0; j <= 90; j+= step) {
  //  pushMatrix();
  //  rotateZ(PI/2);
  //  translate(0, 0, r*sin(radians(j)));
  //  stroke(0, 50);
  //  noFill();
  //  ellipse(0, 0, 2*r*cos(radians(j))+1, 2*r*cos(radians(j))+1);
  //  popMatrix();
  //  pushMatrix();
  //  translate(0, 0, -r*sin(radians(j)));
  //  stroke(0, 50);
  //  noFill();
  //  ellipse(0, 0, 2*r*cos(radians(j)), 2*r*cos(radians(j)));
  //  popMatrix();
  //}
}
