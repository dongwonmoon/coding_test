import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9\-_\.]', '', new_id)
    
    temp = []
    count = 0
    for i, s in enumerate(new_id):
        if s == ".":
            count += 1
            if count >= 2:
                temp.pop()
        else:
            count = 0
        temp.append(s)
    
    while len(temp) > 0 and temp[0] == ".":
        del temp[0]
    while len(temp) > 0 and temp[-1] == ".":
        del temp[-1]
        
    if temp == []:
        temp.append("a")
    
    if len(temp) >= 16:
        temp = temp[:15]
        while temp[-1] == ".":
            temp.pop()
    
    while len(temp) < 3:
        temp.append(temp[-1])
    
    return "".join(temp)