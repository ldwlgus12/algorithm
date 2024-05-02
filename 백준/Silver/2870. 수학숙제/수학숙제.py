n = int(input())
lst = []

for i in range(n):
    num = input()
    result = ''
    
    for j in num:
        # isdigit() 함수를 사용해 해당 값이 문자인지 숫자인지 구별함
        if j.isdigit():
            result += j
        else:
            if result != '':
                lst.append(int(result))
                result = ''
                
    if result != '':
        lst.append(int(result))

lst.sort()

for i in lst:
    print(i)
    