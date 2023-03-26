from itertools import product

def solution(word):
    wlist = []

    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            wlist.append(''.join(list(j)))

    wlist.sort()
    return wlist.index(word) + 1