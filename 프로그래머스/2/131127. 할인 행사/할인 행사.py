from collections import defaultdict

def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    current = defaultdict(int)
    count = 0

    # 초기 윈도우 설정
    for item in discount[:10]:
        current[item] += 1

    def is_valid():
        for item in want_dict:
            if current[item] < want_dict[item]:
                return False
        return True

    if is_valid():
        count += 1

    # 슬라이딩 윈도우
    for i in range(10, len(discount)):
        out_item = discount[i - 10]
        in_item = discount[i]
        
        current[out_item] -= 1
        if current[out_item] == 0:
            del current[out_item]
        current[in_item] += 1

        if is_valid():
            count += 1

    return count
