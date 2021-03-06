def PeriodicCubicSpline():
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

    if y[0] != y[-1]:
        print "y_0 and y_n are not the same. Condition failed. Aborting"
        exit(0)

    print "Periodic Cubic Spline"
    h =[x[i]-x[i-1] for i in range(1,len(x))]
    g = [(y[i]-y[i-1])/h[i-1] for i in range(1,len(x))]

    G = [6*(g[i]-g[i-1]) for i in range(1,len(g))]
    H = []
    for i in range(len(h)-1):
        row = [0 for t in range(i)] + [h[i],2*(h[i]+h[i+1]),h[i+1]] + [0 for t in range(len(h)-2-i)]
        H.append(row)
    import numpy as np
    H = np.array(H)

    # Periodic Spline
    G = [6*(g[0]-g[-1])] + G 
    H = np.delete(H,np.s_[-1],axis=1)
    H = np.delete(H,np.s_[-1],axis=0)
    H = H.tolist()
    H = [ [2*(h[-1]+h[0]),h[0]] + [0 for t in range(len(H[0])-3)] + [h[-1]] ] + H + [ [h[-1]] + [0 for t in range(len(H[0])-3)] + [h[-2],2*(h[-2]+h[-1])] ]
    sigma = np.linalg.solve(H,G).tolist()
    sigma = sigma + [sigma[0]]

    A = [sigma[i+1]/(6*h[i]) for i in range(len(h))]
    B = [sigma[i]/(6*h[i]) for i in range(len(h))]
    C = [(y[i+1]/h[i])-(sigma[i+1]*h[i]/6) for i in range(len(h))]
    D = [(y[i]/h[i])-(sigma[i]*h[i]/6) for i in range(len(h))]
    def get_prediction(x,y,h,sigma,xstar):
        try:
            i = next(v[0] for v in enumerate(x) if v[1] > xstar)
            return (A[i-1]*(xstar - x[i-1])**3) - (B[i-1]*(xstar-x[i])**3)+(C[i-1]*(xstar-x[i-1])) - (D[i-1]*(xstar-x[i]))
        except:
            return y[-1]

    
    yt = []
    for xstar in xt:
        ystar = get_prediction(x,y,h,sigma,xstar)
        yt.append(ystar)
        print xstar,"\t",ystar

    import random
    t = [random.random()*(max(x) - min(x)) + min(x) for i in range(100*len(x))] + x
    t.sort()
    ty = [get_prediction(x,y,h,sigma,t[i]) for i in range(len(t))]


    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("Periodic Cubic Spline")
    ax.set_ylabel("Y")
    ax.set_xlabel("X")
    ax.plot(t,ty, "-", label='Periodic Spline')
    ax.scatter(xt,yt, s=90, c='r', marker="o",label="Test Points")
    ax.scatter(x,y, s=90, c='b', marker="s",label="Original Data")
    plt.legend(loc='best')
    plt.show()
    fig.savefig("Periodic Cubic Spline Plot.png")