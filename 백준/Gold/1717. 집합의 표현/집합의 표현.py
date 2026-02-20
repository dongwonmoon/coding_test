import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1


out = []
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        out.append("YES" if find(a) == find(b) else "NO")

print("\n".join(out))
