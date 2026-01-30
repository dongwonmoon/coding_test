import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    inp = input()
    while "()" in inp:
        inp = inp.replace("()", "")
    inp = inp.replace("\n", "")
    if inp == "":
        print("YES")
    else:
        print("NO")