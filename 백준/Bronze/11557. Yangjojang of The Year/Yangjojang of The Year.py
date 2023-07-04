T = int(input())

for _ in range(T):
    n = int(input())
    m = 0
    school = []
    result = 0

    for i in range(n):
        school.append(list(input().split()))
    
    for j in school:
        if int(j[1]) > m:
            m = int(j[1])
            result = j[0]

    print(result)