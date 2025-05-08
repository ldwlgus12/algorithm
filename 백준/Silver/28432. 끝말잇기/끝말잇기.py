n = int(input())
s = []

for i in range(n):
    s.append(input())
    
m = int(input())
candi = []

for i in range(m):
    candi.append(input())

if "?" in s:
    i = s.index("?")
    if i == 0:
        first = ""
    else:
        first = s[i-1][-1]
    
    if i == len(s)-1:
        last = ""
    else:
        last = s[i+1][0]

    for i in candi:
        if i not in s:
            if (not first or i[0] == first) and (not last or i[-1] == last):
                print(i)
                