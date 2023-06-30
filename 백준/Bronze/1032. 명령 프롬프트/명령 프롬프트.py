N = int(input())
word = list(input())
word_len = len(word)
             
for i in range(N - 1):
    a = list(input())
    for j in range(word_len):
        if word[j] != a[j]:
            word[j] = '?'

print(''.join(word))