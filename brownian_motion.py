def brownian_motion(mu,sigma,paths,points,interval):
    rng=np.random.default_rng()
    Z=rng.normal(mu,sigma,(paths,points))
    dt=(interval[1]-interval[0])/(points-1)
    t_axis=np.linspace(interval[0],interval[1],points)
    W=np.zeros((paths,points))
    for idx in range(points-1):
        W[:,idx+1]=W[:,idx]+mu*dt+sigma*(np.sqrt(dt))*Z[:,idx]
    final_values=pd.DataFrame({"final_values":W[:,-1]})
    return W,final_values
