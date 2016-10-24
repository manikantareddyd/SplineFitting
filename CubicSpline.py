x = []
y = []
xt = []
with open("input.txt") as f:
    for line in f:
        if line == "\n": break
        x.append(float(line.split(" ")[0]))
        y.append(float(line.split(" ")[1]))
    for line in f:
        if line == "\n": break
        xt.append(float(line.split(" ")[0]))
    for line in f:
        so = float(line.split(" ")[0])
        sn = float(line.split(" ")[1])

xy = zip(x,y)
xy.sort()
y = [a for b,a in xy]
x = [b for b,a in xy]

print len(x),len(y)
h =[x[i]-x[i-1] for i in range(1,len(x))]
print h
g = [(y[i]-y[i-1])/h[i-1] for i in range(1,len(x))]

G = [6*(g[i]-g[i-1]) for i in range(1,len(g))]
print len(G)
H = []
for i in range(len(h)-1):
    row = [0 for t in range(i)] + [h[i],2*(h[i]+h[i+1]),h[i+1]] + [0 for t in range(len(h)-2-i)]
    H.append(row)

import numpy as np
H = np.array(H)

# Natural Spline
H = np.delete(H, np.s_[0], axis=1)
H = np.delete(H,np.s_[-1],axis=1)

sigma = np.linalg.solve(H,G)
print sigma