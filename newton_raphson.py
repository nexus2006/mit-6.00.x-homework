epsilon = 0.01
y = 24.0
g = y/2.0

while abs(g*g - y) >= epsilon: #check are we close enough
    print(str(g)+' : '+str(g**2-y)+' : '+str(2*g))
    g = g - (((g**2) - y)/(2*g))
print('sqrt of ' + str(y) + ' is about ' + str(g))
