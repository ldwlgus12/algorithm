def pal():
    n = int(input())
    lst = [input() for _ in range(n)]
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                word = lst[i] + lst[j]
                if word == word[::-1]:
                    return word
    return 0

t = int(input())

while t > 0:
    result = pal()
    if result == 0:
        print(0)
    else: 
        print(result)
    t -= 1