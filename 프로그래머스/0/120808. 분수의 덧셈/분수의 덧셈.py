import math
def solution(numer1, denom1, numer2, denom2):
    num = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(num, denom)
    return [int(num/gcd), int(denom/gcd)]