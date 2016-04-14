# Time to rewrite my final year project program!

import math

increment = 36000 #2PI/increment is the step size around the circle
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

    print(result[2])

    for x in result:
        result[x] = sorted(result[x], key = result[x].get)

    print(result[2])

    fin_len = [] # simply used to check how many unique flags we get

    for key in range(min(result), max(result)):
        if result[key] != result[key+1]:
            fin_len.append(key*360/increment)
            #print(key*360/increment) #uncomment to see what the angles are

    return len(fin_len) # the number of points we get at a given symmetric power

for i in range(1, 41):
    print(calculator(i))
    print('')
