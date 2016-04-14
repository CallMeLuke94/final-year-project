# Time to rewrite my final year project program!

i = 1
R = 200
r = 10
j = 0

import math

increment = 3600 #2PI/increment is the step size around the circle
radius = 100

# this function generates the coefficients of a,b,a-b
def coefficients(n): 
    result = []
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                if (i+j+k == n):
                    result.append([k, j, i])
    return result

# these functions are the elements in our expressions (in polar coordinates)
def a(x):
    return math.sin(x*2*math.pi/increment)*radius

def b(x):
    return math.cos(x*2*math.pi/increment)*radius

def c(x):
    return a(x) - b(x)

# now the real calculations begin
def calculator(sp):
    coef = coefficients(sp)

    # this function defines our inequalities
    def inequality(n, t):
        return a(t)*int(coef[n][0]) + b(t)*int(coef[n][1]) + c(t)*int(coef[n][2])

    indexes = [] # the angles
    values = [] # the values of a,b,a-b for a given angle
    result = {} # holds the values of a,b,a-b at a particular angle

    for t in range(increment):
        indexes.append(t)
        values.append(t)
        expressions = {} # lables the elements: 0->a, 1->b, 2->a-b 
        for n in range(len(coef)):
            expressions[n+1] = round(inequality(n, t), 3)
            values[t] = expressions
        result[indexes[t]] = values[t]

    for x in result:
        result[x] = sorted(result[x], key = result[x].get)

    fin_len = [] # simply used to check how many unique flags we get
    points = []
    for key in range(min(result), max(result)):
        if result[key] != result[key+1]:
            fin_len.append(key*360/increment) # the length of this is the number of points we get at a given symmetric power
            points.append(key*360/increment) #uncomment to see what the angles are

    return points 

# for i in range(1, 41):
#    print(calculator(i))
#    print('')


def setup():
    size(430, 430)
    smooth()
    frameRate(5)
  
    background(150, 150, 200)
    stroke(0)
    noFill()
    ellipse(width/2, height/2, R*2, R*2)
    
    noLoop()
    
def draw():
    background(150, 150, 200)
    stroke(0)
    noFill()
    ellipse(width/2, height/2, R*2, R*2)
    pushMatrix();
    translate(width/2, height/2)
    for theta in calculator(i):
        A = 0 #(90-theta)%90
        x = R*cos(radians(theta-A))
        y = R*sin(radians(theta-A))
        noStroke()
        fill(255)
        ellipse(x, -y, r, r)
        global j
        j = j + 1
        #print(theta)
    popMatrix()
    
    noStroke();
    fill(150, 150, 200);
    rectMode(CENTER);
    rect(width/2, height/2, 250, 250);
 
    textAlign(CENTER);
    noStroke();
    fill(255);
    textSize(18);
    text("Symmetric Power: " + str(i), width/2, height/2 - 50);
    textSize(20);
    text("Number of points: " + str(j), width/2, height/2);

def mousePressed():
    save("sl3image.png")
    print("image saved")

def keyPressed():
    global i
    global j
    if (key == CODED):
        if (keyCode == UP):
            global i
            global j
            i = i + 1
            j = 0
            redraw()
        if (keyCode == DOWN):
            if (i > 0):
                i = i - 1
                j = 0
                redraw()
            else:
                i = 0