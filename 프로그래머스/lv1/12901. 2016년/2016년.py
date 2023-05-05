def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']  # 1월 1일이 금요일이므로 금요일부터 시작
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 월의 일수를 리스트로 저장
    days_passed = sum(months[:a-1]) + b - 1  # 입력된 월까지의 일수와 일(day)을 더해서 전체 일 수를 계산
    return days[days_passed % 7]  # 전체 일 수를 7로 나눈 나머지를 인덱스로 사용하여 요일 반환


#문제가 약간 어려움 이해가 필요해서 한번더 풀어봐야함 풀이를 봤음
