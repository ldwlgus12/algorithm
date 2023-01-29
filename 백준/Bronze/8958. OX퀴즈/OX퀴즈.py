N = int(input())

for i in range(N):
    result = 0
    sum = 0
    string = list(input())

    for j in range(len(string)):
        if string[j] == 'O':
            result += 1
            sum += result
        else:
            result = 0
    
    print(sum)