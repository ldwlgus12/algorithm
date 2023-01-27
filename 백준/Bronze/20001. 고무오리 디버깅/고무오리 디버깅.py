start = input()
result = 0

while True:
    string = input()
    if string == '문제':
        result += 1
    elif string == '고무오리':
        if result == 0:
            result += 2
        else:
            result -= 1
    elif string == '고무오리 디버깅 끝':
        break

if result > 0:
    print('힝구')
else:
    print('고무오리야 사랑해')