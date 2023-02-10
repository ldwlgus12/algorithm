T = int(input())
for i in range(1, T+1):
    n = int(input())
    card = list(input().split())
    card1 = []
    card2 = []
    card3 = []
    if len(card)%2 == 0:
        card1.append(card[:len(card)//2])
        card2.append(card[(len(card)//2):])
    else:
        card1.append(card[:(len(card)//2)+1])
        card2.append(card[(len(card)//2)+1:])
    
    s1 = card1[0]
    s2 = card2[0]


    if len(card)%2 == 0:
        for a in range(len(s1)):
            card3.append(s1[a])
            card3.append(s2[a])
        print(f'#{i}', *card3)
    else:
        for a in range(len(s2)):
            card3.append(s1[a])
            card3.append(s2[a])
        card3.append(s1[-1])
        print(f'#{i}',*card3)