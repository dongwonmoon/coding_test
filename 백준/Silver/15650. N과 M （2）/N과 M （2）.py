N, M = map(int, input().split())


def build(path, n):
    if len(path) == M:
        print(*path)
        return

    for i in range(n, N + 1):
        path.append(i)
        build(path, i + 1)
        path.pop()


build([], 1)