<<<<<<< HEAD
sp = 2  #the symmetric power we are in
lmd = [1, -1, 0] #our choice of lambda

def dot(x, y): #dot product function
=======
sp = 2
lmd = [1, -1, 0]

def dot(x, y):
>>>>>>> origin/master
    if len(x) != len(y):
        return 'Vectors must be the same length'
    else:
        d = []
        for i in range(len(x)):
            d.append(x[i]*y[i])
        return sum(d)

<<<<<<< HEAD
def filter(x): #removes duplicates from a list
=======
def filter(x):
>>>>>>> origin/master
    dist = [x[0]]
    for i in x:
        if i not in dist:
            dist.append(i)
    return dist

<<<<<<< HEAD
def X1(a, b):   #these 3 functions generate the Xi's in (3.1)
=======
def X1(a, b):
>>>>>>> origin/master
    return 2*(a[0]-b[0])+(a[1]-b[1])+(a[2]-b[2])

def X2(a, b):
    return (a[0]-b[0])+2*(a[1]-b[1])+(a[2]-b[2])

def X3(a, b):
    return (a[0]-b[0])+(a[1]-b[1])+2*(a[2]-b[2])

def coefficients(n):
    result = []
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                if (i+j+k == n):
                    result.append([k, j, i])
    return result

def point(r, lam):
    V = coefficients(r)
    final = []

    for x in range(len(V)):
        for y in range(x+1, len(V)):
            final.append([X1(V[x], V[y]), X2(V[x], V[y]), X3(V[x], V[y])])

<<<<<<< HEAD
=======
    #print(final)

>>>>>>> origin/master
    result = []
    for n in final:
        if dot(n, lam) == 0:
            result.append(n)

    return result

for r in range(2, 4):
    P = filter(point(r, lmd))
    print('Symmetric Power %s:' % r)
    for n in P:
        print(n)
    print('')
<<<<<<< HEAD
=======

# point(sp, lmd)
>>>>>>> origin/master
