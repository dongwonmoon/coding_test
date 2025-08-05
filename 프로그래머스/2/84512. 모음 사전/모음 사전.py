def solution(word):
    items1 = ["A", "E", "I", "O", "U"]
    items2 = ["", "A", "E", "I", "O", "U"]
    dictionary = []
    for item1 in items1:
        for item2 in items2:
            for item3 in items2:
                for item4 in items2:
                    for item5 in items2:
                        dictionary.append(item1+item2+item3+item4+item5)
    
    dictionary = sorted(list(set(dictionary)))
    
    return dictionary.index(word) + 1        
    