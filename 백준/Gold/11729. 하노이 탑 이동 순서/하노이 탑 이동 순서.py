import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

print(str(2**N - 1) + "\n")


def hanoi(n, start, end, aux):
    if n == 1:
        print(str(start) + " " + str(end) + "\n")
        return

    hanoi(n - 1, start, aux, end)
    print(str(start) + " " + str(end) + "\n")
    hanoi(n - 1, aux, end, start)


hanoi(N, 1, 3, 2)