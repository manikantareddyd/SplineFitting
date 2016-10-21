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

print "Linear Spline"
for xstar in xt:
    i = next(v[0] for v in enumerate(x) if v[1] > xstar)
    ystar = ((xstar - x[i-1])*y[i]/(x[i]-x[i-1])) + ((xstar - x[i])*y[i-1]/(x[i-1]-x[i]))
    print xstar,"\t",ystar
