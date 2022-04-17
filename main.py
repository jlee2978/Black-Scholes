import math
from scipy import stats
from scipy.stats import norm

def main():
    # s = stock price, k = strike price, r = interest rate in %, t = years to expiry, vol annual volatility in %
    # after asking for risk free rate, divide by 100
    # after asking for days, convert to time in years
    
    s = float(input("Stock spot price: "));
    k = float(input("Strike price: "));
    r = float(input("Risk free rate (%): "));
    t = float(input("Days to expiry: "));
    vol = float(input("Volatility: "));

    put(s, k, r/100, t/365, vol/100);

def call (s, k, r, t, vol):
    # s = stock price, k = strike price, r = risk free rate in %, t = years to expiry, vol = annual volatility in %
    
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

    # calculate d1 and d2
    d1 = (math.log(s/k) + (r + (vol**2)/2) * t) / (vol * math.sqrt(t));
    d2 = d1 - vol * math.sqrt(t);

    p = norm.cdf(-d2) * k * math.exp(-r*t) - norm.cdf(-d1) * s;
    print(p);
    return p;

# unused
def cdf(d):
    # to fix
    # N = math.erf(d / math.sqrt(2.0));
    # return (1 + erf(d / sqrt(2.0))) / 2.0;
    return stats.norm.cdf(d);
    # return N;

main();