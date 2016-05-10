import math

increment1 = 180 #PI/increment1 is the step size around the sphere
increment2 = 360 #2PI/increment2 is the step size around each great circle
radius = 100

# this function generates the coefficients of a,b,c,a-b-c
def coefficients(n):
    result = []
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                for l in range(n-i-j-k+1):
                   if (i+j+k+l == n):
                        result.append([l, k, j, i])
    return result

# these functions are the elements in our expressions (in polar coordinates)
def a(theta, phi):
    theta = theta*math.pi/increment1
    phi = phi*2*math.pi/increment2
    return radius*math.sin(theta)*math.cos(phi)

def b(theta, phi):
    theta = theta*math.pi/increment1
    phi = phi*2*math.pi/increment2
    return radius*math.sin(theta)*math.sin(phi)

def c(theta):
    theta = theta*math.pi/increment1
    return radius*math.cos(theta)

def d(theta, phi):
    return a(theta, phi) - b(theta, phi) - c(theta)

# this function does the main calculations
def calculator(sp):
    coef = coefficients(sp)

    #this function defines our inequalities
    def inequality(n, t, s):
        return(a(t, s)*int(coef[n][0]) + b(t, s)*int(coef[n][1]) + c(t)*int(coef[n][2]) + d(t, s)*int(coef[n][3]))

    indexes = [] # the angles around a given circle
    values = [] # the values of a,b,c,a-b-c at a given angle
    circles = {} # the values and angles for a given great circle
    flags = {} # where we store the flags
    result = {} # the values and angles for every circle

    for t in range(increment1):
        for s in range(increment2):
            indexes.append(s)
            values.append(s)
            expressions = {} # lables the elements a,b,c,d
            for n in range(len(coef)):
                expressions[n+1] = round(inequality(n, t, s), 3)
                values[s] = expressions
            circles[indexes[s]] = values[s]

        for x in circles:
            circles[x] = sorted(circles[x], key = circles[x].get)

        flags[t] = circles

        cir_len = []
        final = []
        circle_keys = []

        for key in range(min(circles), max(circles)):
            if circles[key] != circles[key+1]:
                cir_len.append(round(key*360/increment2, 3))
                circle_keys.append(key)
                result[t] = circle_keys
                #print(key, t)

        final.append(cir_len)

    return result #flags

file = open("results.txt", "w") #write the results to a text file
for value in calculator(1): #change 1 to whichever symmetric power you want
    file.write(str(calculator(1)[value])+'\n')
file.close()

#each new line of this file is an angle of longditude, each entry on a given line is an angle of latitude

#to print a particular flag change line 78 to "return flags" and then uncomment the following line:
#print(calculator(n)[theta][phi])
