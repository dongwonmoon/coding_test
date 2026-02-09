N = int(input())

if N == 1:
    print(1)
    exit()

a = [0] * N
a[0] = 1
a[1] = 2

for i in range(2, N):
    a[i] = a[i - 1] + a[i - 2]

print(a[-1] % 10007)