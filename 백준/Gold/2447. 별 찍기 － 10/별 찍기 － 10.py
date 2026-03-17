import sys

N = int(input())
k = 1
pattern = "*"

while 3**k <= N:
    top = [line * 3 for line in pattern]
    mid = [line + " " * len(line) + line for line in pattern]
    bottom = [line * 3 for line in pattern]
    pattern = top + mid + bottom
    k += 1

for line in pattern:
    sys.stdout.write(line + "\n")
