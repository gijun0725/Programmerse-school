def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        if i.upper() in cache:
            cache.remove(i.upper())
            cache.append(i.upper())
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(i.upper())
            answer += 5

    return answer
