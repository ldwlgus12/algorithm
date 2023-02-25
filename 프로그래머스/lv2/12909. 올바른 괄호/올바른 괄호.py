def solution(s):
    answer = True
    m = 0
    
    for i in range(len(s)):
        if s[0] == ')' or s[-1] == '(':
            answer = False
            break

        if s[i] == '(':
            m += 1
        else:
            m -= 1
            if m < 0:
                answer = False
                break

    if s[0] == '(' and s[-1] == ')':
        if m == 0:
            answer = True
        else:
            answer = False
    
    return answer