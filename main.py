import math
from scipy import stats
from scipy.stats import norm

def call (s, k, r, t, vol):
    # s = stock price, k = strike price, r = risk free rate in %, t = years to expiry, vol = annual volatility in %
    # after asking for risk free rate, divide by 100
    # after asking for days, convert to time in years

    # calculate d1 and d2
    d1 = (math.log(s/k) + (r + (vol**2)/2) * t) / (vol * math.sqrt(t));
    d2 = d1 - vol * math.sqrt(t);
    c = norm.cdf(d1) * s - norm.cdf(d2) * k * math.exp(-r*t);
    print(c);
    return c;

def put (s, k, r, t, vol):
    # initialize p as a test
    p = 0;

    # s = stock price, k = strike price, r = risk free rate in %, t = years to expiry, vol = annual volatility in %
    # after asking for risk free rate, divide by 100
    # after asking for days, convert to time in years

    # calculate d1 and d2
    d1 = (math.log(s/k) + (r + (vol**2)/2) * t) / (vol * math.sqrt(t));
    d2 = d1 - vol * math.sqrt(t);

    p = norm.cdf(-d2) * k * math.exp(-r*t) - norm.cdf(-d1) * s;
    print(p);
    return p;

# unused for now
def cdf(d):
    # to fix
    # N = math.erf(d / math.sqrt(2.0));
    # return (1 + erf(d / sqrt(2.0))) / 2.0;
    return stats.norm.cdf(d);
    # return N;

# s = stock price, k = strike price, r = interest rate in %, t = years to expiry, vol annual volatility in %
put(100, 100, 0.0033, 0.1, 0.25);