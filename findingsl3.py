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

# now the calculations begin
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
            fin_len.append(key*360/increment)
            points.append(key*360/increment) #uncomment to see what the angles are

    return points #len(fin_len)

file = open("results.txt", "w") #write the results to a text file
for n in range(1, 51): #change 51 to whichever symmetric power you want
    file.write(str(calculator(n))+'\n')
file.close()

#each new line of the text file shows a list of angles for the points at that symmetric power

#to see only the number of points at a given symmetric power, change line 57 to "return len(fin_len)" and then uncomment the following:
#for n in range(1, 51):
#   print(calculator(n))
