for _ in range(0, int(input())):
    letter = input()
    n = int(len(letter) ** (1/2))
    result = ""
    
    for i in range(n, 0, -1):
        for j in range(i, n*n+1, n):
            result += letter[j-1]

    print(result)
    