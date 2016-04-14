# Lets do SL_4!

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

# now we calculate
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

    # for n in result:
    #     print(n, result[n])

    return flags

print(calculator(3)[157][286])

n = len(coefficients(3))
thing = {}

for i in range(n):
    thing[i] = coefficients(3)[i]
    print(i+1, thing[i])


#most recent: [157][286] giving [10, 9, 8, 7, 6, 5, 16, 4, 3, 2, 15, 1, 14, 13, 12, 11, 19, 18, 17, 20]
#previous attempt was [155][350]
#[25][10] gave the first triangle?

# 1 [3, 0, 0, 0]
# 2 [2, 1, 0, 0]
# 3 [1, 2, 0, 0]
# 4 [0, 3, 0, 0]
# 5 [2, 0, 1, 0]
# 6 [1, 1, 1, 0]
# 7 [0, 2, 1, 0]
# 8 [1, 0, 2, 0]
# 9 [0, 1, 2, 0]
# 10 [0, 0, 3, 0]
# 11 [2, 0, 0, 1]
# 12 [1, 1, 0, 1]
# 13 [0, 2, 0, 1]
# 14 [1, 0, 1, 1]
# 15 [0, 1, 1, 1]
# 16 [0, 0, 2, 1]
# 17 [1, 0, 0, 2]
# 18 [0, 1, 0, 2]
# 19 [0, 0, 1, 2]
# 20 [0, 0, 0, 3]
