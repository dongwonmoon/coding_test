N = int(input())

A = list(map(int, input().split()))
D = [A[0]]

for item in A[1:]:
    if item > D[-1]:
        D.append(item)
    else:
        lo, hi = 0, len(D) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if D[mid] < item:
                lo = mid + 1
            else:
                hi = mid - 1

        D[lo] = item

print(len(D))