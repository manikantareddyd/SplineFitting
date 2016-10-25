def QuadraticSpline():
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

    print "Quadratic Spline"
    import numpy as np
    n = len(x)
    A = np.tri(n,n) - np.tri(n,n,-2)
    A = A.astype(float)

    A = np.delete(A,np.s_[0],axis=0)
    A = A.tolist()
    A = [[1,-1]+[0 for i in range(len(A[0])-2)]] + A

    d = [0]
    for i in range(1,n):
        d.append( 2*(y[i]-y[i-1])/(x[i]-x[i-1]))
    d = np.array(d)
    z = np.linalg.solve(A,d).tolist()

    def get_prediction(x,y,z,xstar):
        try:
            i = next(v[0] for v in enumerate(x) if v[1] > xstar)
            return (z[i-1]*(xstar - x[i-1])) + ((z[i]-z[i-1])*((xstar - x[i-1])**2)/(2*(x[i]-x[i-1]))) + y[i-1]
        except:
            return y[-1]


    yt = []
    for xstar in xt:
        ystar = get_prediction(x,y,z,xstar)
        yt.append(ystar)
        print xstar,"\t",ystar

    import random
    t = [random.random()*(max(x) - min(x)) + min(x) for i in range(100*len(x))] + x
    t.sort()
    ty = [get_prediction(x,y,z,t[i]) for i in range(len(t))]


    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("Quadratic Spline")
    ax.set_ylabel("Y")
    ax.set_xlabel("X")
    ax.plot(t,ty, "-", label='Quadratic Spline')
    ax.scatter(xt,yt, s=90, c='r', marker="o",label="Test Points")
    ax.scatter(x,y, s=90, c='b', marker="s",label="Original Data")
    plt.legend(loc='best')
    plt.show()
    fig.savefig("Quadratic Spline Plot.png")
