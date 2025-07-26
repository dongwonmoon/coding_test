def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            ind = cache.index(city)
            cache = cache[:ind] + cache[ind+1:] + [cache[ind]]
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
        
    return answer