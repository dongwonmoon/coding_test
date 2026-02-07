import sys

input = sys.stdin.readline

T = int(input())

table = {1: 1, 2: 2, 3: 4}

for i in range(4, 11):
    count = 0
    m1 = i - 1
    m2 = i - 2
    m3 = i - 3

    count += table[m1] + table[m2] + table[m3]

    table[i] = count

for _ in range(T):
    print(table[int(input())])