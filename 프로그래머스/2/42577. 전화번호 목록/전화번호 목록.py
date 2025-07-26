def solution(phone_book):
    # 모든 전화번호를 해시셋에 저장
    phone_set = set(phone_book)

    # 각 번호에 대해, 길이가 1부터 (len-1)까지의 접두사만 해시셋에 있는지 확인
    for number in phone_book:
        # 접두사 길이 i: 1, 2, ..., len(number)-1
        for i in range(1, len(number)):
            if number[:i] in phone_set:
                # 어떤 다른 번호가 현재 번호의 접두사라면 False
                return False

    # 모든 검사 통과 시 True
    return True