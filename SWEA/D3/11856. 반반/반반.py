T = int(input())
for i in range(1, T+1):
    word = list(input())
    cnt_ = 0
    
    for j in range(len(word)):
        cnt = word.count(word[j])
        cnt_ += cnt

    if cnt_ == 8:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')  