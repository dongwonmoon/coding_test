import sys

input = sys.stdin.readline

while True:
    inp = input().rstrip("\n")
    if inp == ".":
        break

    stack = []
    ok = True

    for s in inp:
        if s in ("(", "["):
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                ok = False
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                ok = False
                break

    print("yes" if ok and not stack else "no")