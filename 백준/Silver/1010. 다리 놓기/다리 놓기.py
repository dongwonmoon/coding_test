import sys
from functools import lru_cache


@lru_cache
def fact(num):
    return num * fact(num - 1) if num > 1 else 1


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(int(fact(M) / (fact(N) * fact(M - N))))