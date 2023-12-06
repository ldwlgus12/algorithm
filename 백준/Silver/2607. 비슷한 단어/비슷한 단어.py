n = int(input())
word = list(input())
result = 0

for i in range(n-1):
    compare = input()
    word_copy = word[:] 
    cnt = 0

    for j in compare:
        if j in word_copy:
            word_copy.remove(j)
        else:
            cnt += 1

    if cnt < 2 and len(word_copy) < 2:
        result += 1

print(result)
