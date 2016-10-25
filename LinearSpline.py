def LinearSpline():
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

    xy = zip(x,y)
    xy.sort()
    y = [a for b,a in xy]
    x = [b for b,a in xy]

    print "Linear Spline"
    def get_prediction(x,y,xstar):
        try:
            i = next(v[0] for v in enumerate(x) if v[1] > xstar)
            return ((xstar - x[i-1])*y[i]/(x[i]-x[i-1])) + ((xstar - x[i])*y[i-1]/(x[i-1]-x[i]))
        except:
            return y[-1]
        
    yt = []
    for xstar in xt:
        ystar = get_prediction(x,y,xstar)
        yt.append(ystar)
        print xstar,"\t",ystar
    import random
    t = [random.random()*(max(x) - min(x)) + min(x) for i in range(100*len(x))] + x
    t.sort()
    ty = [get_prediction(x,y,t[i]) for i in range(len(t))]


    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("Linear Spline")
    ax.set_ylabel("Y")
    ax.set_xlabel("X")
    ax.plot(t,ty, "-", label='Linear Spline')
    ax.scatter(xt,yt, s=90, c='r', marker="o",label="Test Points")
    ax.scatter(x,y, s=90, c='b', marker="s",label="Original Data")
    plt.legend(loc='best')
    plt.show()
    fig.savefig("Linear Spline Plot.png")