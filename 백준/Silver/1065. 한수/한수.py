N = int(input())

if N == 1:
    print(1)
    exit()


def check_hansu(num):
    if num // 10 < 10:
        return 1

    l = list(map(int, ".".join(str(num)).split(".")))
    prev_a = None
    for i in range(1, len(l)):
        a = l[i] - l[i - 1]
        if prev_a is not None and a != prev_a:
            return 0
        prev_a = a

    return 1


answer = 0
for i in range(1, N + 1):
    answer += check_hansu(i)

print(answer)