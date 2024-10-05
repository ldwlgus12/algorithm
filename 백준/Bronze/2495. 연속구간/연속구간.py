for i in range(3):
    num = input()
    cnt = 1
    result = 0
    
    for j in range(1, len(num)):
        if num[j-1] == num[j]:
            cnt += 1
        else:
            cnt = 1

        if cnt > result:
            result = cnt
            
    print(result)