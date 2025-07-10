def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    while len(A) > 0:
        answer += A[0] * B[0]
        A.pop(0)
        B.pop(0)
    return answer
        