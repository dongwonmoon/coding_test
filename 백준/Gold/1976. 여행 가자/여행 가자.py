import sys


def find(x):
    if x != parent[x]:
        parent[x] = parent[parent[x]]
        return find(parent[x])

    return x


def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if rank[ra] > rank[rb]:
        parent[rb] = ra
    elif rank[ra] < rank[rb]:
        parent[ra] = rb
    else:
        parent[rb] = ra
        rank[ra] += 1


input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

for i in range(N):
    for j, t in enumerate(map(int, input().split())):
        if t:
            union(i + 1, j + 1)

itinery = list(map(int, input().split()))

for i in range(1, M):
    u, v = itinery[i - 1], itinery[i]

    if parent[u] != parent[v]:
        print("NO")
        exit()

print("YES")