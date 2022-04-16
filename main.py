import math

def call (s, k, r, t, vol):
    # initalizing c as 0 as a test
    c = 0;

    # s = stock price, k = strike price, r = interest rate in %, t = years to expiry

    # giving test values for variables
    s = 100;
    k = 105;
    r = 0.025;
    t = 0.1;    # after asking for days, convert to time in years

    # calculate d1 and d2
    d1 = (math.log(s/k) + (r + vol**2/2) * t) / (vol * math.sqrt(t));
    d2 = d1 - vol * math.sqrt(t);

    c = cdf(d1) * s - cdf(d2) * k * math.exp(-r*t);
    print(c);
    return c;


def cdf(d):
    # to fix
    N = math.erf(d / math.sqrt(2.0));
    # return (1 + erf(d / sqrt(2.0))) / 2.0;
    return N;