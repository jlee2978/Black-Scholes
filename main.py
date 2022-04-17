import math
from scipy import stats
from scipy.stats import norm

def main():
    # s = stock price, k = strike price, r = interest rate in %, t = years to expiry, vol annual volatility in %    
    s = float(input("Stock spot price: "));
    k = float(input("Strike price: "));
    r = float(input("Risk free rate (%): "));
    t = float(input("Days to expiry: "));
    vol = float(input("Volatility (%): "));

    call(s, k, r/100, t/365, vol/100);
    put(s, k, r/100, t/365, vol/100);

def call (s, k, r, t, vol):    
    d1 = (math.log(s/k) + (r + (vol**2)/2) * t) / (vol * math.sqrt(t));
    d2 = d1 - vol * math.sqrt(t);
    c = norm.cdf(d1) * s - norm.cdf(d2) * k * math.exp(-r*t);
    print("Call price: " + str(c));
    return c;

def put (s, k, r, t, vol):
    d1 = (math.log(s/k) + (r + (vol**2)/2) * t) / (vol * math.sqrt(t));
    d2 = d1 - vol * math.sqrt(t);
    p = norm.cdf(-d2) * k * math.exp(-r*t) - norm.cdf(-d1) * s;
    print("Put price: " + str(p));
    return p;

main();