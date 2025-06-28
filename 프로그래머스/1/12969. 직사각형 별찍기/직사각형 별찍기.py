a, b = map(int, input().strip().split(' '))
st = ["*" * a + "\n" for _ in range(b)]
print("".join(st))