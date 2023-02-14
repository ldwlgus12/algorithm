import math

def solution(numer1, denom1, numer2, denom2):
    one = numer1 * denom2 + numer2 * denom1
    two = denom1*denom2
    gcd = math.gcd(one, two)    
    return [one//gcd, two//gcd]