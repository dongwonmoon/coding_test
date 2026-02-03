N, K = map(int, input().split())
K -= 1
i = K
l = list(range(1, N + 1))

print("<", end="")
while l:
    while i >= len(l):
        i -= len(l)
    if len(l) == 1:
        print(l[0], end="")
        break
    print(l.pop(i), end=", ")
    i += K

print(">")