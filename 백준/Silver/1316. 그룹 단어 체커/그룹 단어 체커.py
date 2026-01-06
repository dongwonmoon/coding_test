N = int(input())

count = 0

for _ in range(N):
    ss = input()

    for i in range(len(ss)):
        if ss[i + 1 :].find(ss[i]) not in [0, -1]:
            break

    if i == len(ss) - 1:
        count += 1

print(count)
