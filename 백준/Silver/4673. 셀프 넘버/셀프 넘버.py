from functools import reduce

s = set()

for i in range(1, 10000):
    il = list(map(int, str(i)))
    s.add(i + reduce(lambda x, y: x + y, il))

print("\n".join(map(str, sorted(list(set(list(range(1, 10001))) - s)))))
