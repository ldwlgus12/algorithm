from itertools import permutations

def solution(numbers):
    answer = []     
    per = []                              
    num = [n for n in numbers]      #numbers를 하나씩 자른 것        

    for i in range(1, len(numbers)+1):      # numbers의 각 숫자들을 순열로 모든 경우의 수 만들기
        per += list(permutations(num, i))   # i개씩 순열 조합을 만듬

    new_num = [int(('').join(p)) for p in per]  # 각각의 순열 조합을 하나의 int형 숫자로 변환

    for n in new_num:       # new_num에 담은 숫자 각각이 소수인지 판별                  
        if n < 2:           # 만약 n이 2보다 작다면 (0, 1은 소수가 아니므로)
            continue        # 건너뜀

        check = True
        for i in range(2, int(n**0.5) + 1): # n의 제곱근보다 작은 수까지만 나눗셈
            if n % i == 0:                  # 하나라도 나눠떨어진다면 소수가 아님
                check = False
                break
            
        if check:
            answer.append(n)    # 만약 소수라면 리스트에 추가

    return len(set(answer))     # set으로 중복을 제거하고 답을 반환
