import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    age, name = input().split()
    arr.append((int(age), name))

arr.sort(key=lambda x: x[0])
print("\n".join(f"{a} {n}" for a, n in arr))
