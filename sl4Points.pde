float xmag, ymag = 0;
float newXmag, newYmag = 0;
float r = 500;
float phi;
float theta;
float[][] result;
float s = 1;
float g = 10;
float step = 5;
float scl = 600;

PVector v1, v2, v3, v4, v5;

void setup() { 
  size(800, 700, P3D); 

  String[] output = loadStrings("output3.txt");

  result = new float[output.length][1];

  for (int i = 0; i < output.length; i++) {
    output[i] = output[i].substring(1, output[i].length()-2);
    float[] data = float(split(output[i], ", "));
    result[i] = data;


    v2 = new PVector(-5,-1,-9);

    v1 = new PVector(-9, -1, -13);
    v3 = new PVector(-1, 0, -1);    
    v4 = new PVector(-1, 0, -2);    
    v5 = new PVector(-1, 0, -1.5);  //these are the vectors we want!


    v1.normalize();
    v2.normalize();
    v3.normalize();
    v4.normalize();
    v5.normalize();

    v1.mult(scl);
    v2.mult(scl);
    v3.mult(scl);
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
      stroke(0, 0, 0);
      fill(0, 0, 0);
      ellipse(0, 0, s, s);
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
  line(0, 0, 0, v3.x, v3.y, v3.z);
  stroke(0, 242, 251);
  line(0, 0, 0, v1.x, v1.y, v1.z);
  line(0, 0, 0, v2.x, v2.y, v2.z);
  line(0, 0, 0, v4.x, v4.y, v4.z);
  line(0, 0, 0, v5.x, v5.y, v5.z);


  pushMatrix();
  rotateZ(radians(360-170));  //170
  rotateY(radians(180-25));   //25
  translate(0, 0, r+1);
  noStroke();
  fill(#FF8F05); //orange
  ellipse(0, 0, 13, 13);
  popMatrix();

  pushMatrix();
  rotateZ(radians(110-286));  //350
  rotateY(radians(305-157));  //155
  translate(0, 0, r+1);
  noStroke();
  fill(#19CB23); //green
  ellipse(0, 0, 13, 13);
  popMatrix();  

  popMatrix();

  if (keyPressed == true) {
    //save("image.png");
    //println("image saved");
  }
} 

void basis() {
  strokeWeight(2);
  stroke(255, 0, 0);
  fill(255, 0, 0);
  line(-(r+200), 0, (r+200), 0);
  ellipse((r+200), 0, g, g);
  stroke(0, 255, 0);
  fill(0, 255, 0);
  line(0, -(r+200), 0, (r+200));
  ellipse(0, (r+200), g, g);
  pushMatrix();
  rotateY(PI/2);
  stroke(0, 0, 255);
  fill(0, 0, 255);
  line(-(r+200), 0, (r+200), 0);
  ellipse(-(r+200), 0, g, g);
  popMatrix();


  //strokeWeight(0.5);
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