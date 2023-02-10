T = int(input())
for i in range(1, T+1):
    word = list(input())
    word_list =[]

    for j in range(len(word)):
        if word[j] == 'a' or word[j] == 'e' or word[j] == 'i' or word[j] == 'o' or word[j] == 'u':
            pass
        else:
            word_list.append(word[j])
    print(f'#{i} ', *word_list, sep='')