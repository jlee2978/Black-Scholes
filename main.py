import math
from scipy import stats
from scipy.stats import norm

def call (s, k, r, t, vol):
    # initalizing c as 0 as a test
    c = 0;

    # s = stock price, k = strike price, r = risk free rate in %, t = years to expiry, vol = annual volatility in %

    # giving test values for variables
    s = 100;
    k = 100;
    r = 0.0033;
    t = 0.1;    # after asking for days, convert to time in years
    vol = 0.25;

    # calculate d1 and d2
    d1 = (math.log(s/k) + (r + (vol**2)/2) * t) / (vol * math.sqrt(t));
    d2 = d1 - vol * math.sqrt(t);

    c = norm.cdf(d1) * s - norm.cdf(d2) * k * math.exp(-r*t);
    # c = 51.6 - 48.4 * math.exp(-r*t);
    print(d1);
    print(d2);
    print(c);
    return c;

# unused for now
def cdf(d):
    # to fix
    # N = math.erf(d / math.sqrt(2.0));
    # return (1 + erf(d / sqrt(2.0))) / 2.0;
    return stats.norm.cdf(d);
    # return N;

# s = stock price, k = strike price, r = interest rate in %, t = years to expiry, vol annual volatility in %
call(100, 100, 0.33, 0.1, 0.25);