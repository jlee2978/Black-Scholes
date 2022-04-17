import numpy as np
from scipy.stats import norm

N = norm.cdf

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    print(S * N(d1) - K * np.exp(-r*T)* N(d2))
    return 0;

BS_CALL(100,100,0.1,0.33,0.25);