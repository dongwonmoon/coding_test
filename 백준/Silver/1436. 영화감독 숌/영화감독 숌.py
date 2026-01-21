N = int(input())

s = set()
l = len(str(N))
ll = []
for i in range(10**l + 1):
    ll.append(str(i).zfill(l + 1))

for n in ll:
    for i in range(len(n) + 1):
        s.add(int(n[:i] + "666" + n[i:]))

print(sorted(list(s))[N - 1])
