def int_to_base(x, n):
    tmp = []
    while x > 0:
        tmp.append(str(x % 2))
        x //= 2
    while len(tmp) < n:
        tmp.append("0")
    return "".join(reversed(tmp))

def solution(n, arr1, arr2):
    arr1 = list(map(lambda x: int_to_base(x, n), arr1))
    arr2 = list(map(lambda x: int_to_base(x, n), arr2))
    
    decoded_map = []
    for e1, e2 in zip(arr1, arr2):
        st = []
        for i1, i2 in zip(e1, e2):
            if int(i1) == 0 and int(i2) == 0:
                st.append(" ")
            else:
                st.append("#")
        decoded_map.append("".join(st))
        
    return decoded_map
        