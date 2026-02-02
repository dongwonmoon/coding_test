input()

An = {key: 1 for key in map(int, input().split(" "))}

input()

Am = list(map(int, input().split(" ")))

for item in Am:
    print(An.get(item, 0))