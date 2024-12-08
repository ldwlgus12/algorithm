while True:
    n = int(input())
    if n == 0:
        break
 
    lst = [] 
    for i in range(n):
        word = input()
        lst.append(word)
 
    lst.sort(key=str.lower)
    print(lst[0])
