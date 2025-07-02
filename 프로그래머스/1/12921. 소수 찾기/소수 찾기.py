def solution(n):
    primes = [2]
    pr = [2]
    for i in range(2, n + 1):
        if pr[-1] < int(i ** .5):
            pr.append(primes[len(pr)])
        for j, prime in enumerate(pr):
            if i % prime == 0:
                break
            if j == len(pr) - 1:
                primes.append(i)

    return len(primes)