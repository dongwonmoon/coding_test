def get_divider(x):
    divider = set()
    for i in range(1, int(x**.5) + 1):
        if x % i == 0:
            divider.add(i)
            divider.add(x // i)
    return list(divider)

def solution(number, limit, power):
    kk = []
    for x in range(1, number+1):
        divs = len(get_divider(x))
        if divs > limit:
            kk.append(power)
        else:
            kk.append(divs)
    return sum(kk)