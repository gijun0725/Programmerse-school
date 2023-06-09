def solution(phone_book):
    hash_map={}
    for phone_number in phone_book:
        hash_map[phone_number]=1
    for phone_number in phone_book:
        jub=""
        for number in phone_number:
            jub+=number
            if jub in hash_map and jub !=phone_number:
                return False
    return True
    return answer