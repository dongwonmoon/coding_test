from itertools import combinations
from math import gcd

def solution(arr):
    while len(arr) > 1:
        lcm = (arr[-1] * arr[-2]) // gcd(arr[-1], arr[-2])
        arr.pop()
        arr.pop()
        arr.append(lcm)
    
    return arr[0]