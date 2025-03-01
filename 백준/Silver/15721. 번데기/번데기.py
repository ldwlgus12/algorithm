a = int(input())
t = int(input())
bd = int(input())

bbun = 0
daegi = 0
cnt = 0
lst = []          

while True:
    cnt += 1
    for _ in range(2):
        bbun += 1
        lst.append((bbun, 0))
        daegi += 1
        lst.append((daegi, 1))
        
    for _ in range(cnt+1):
        bbun += 1
        lst.append((bbun, 0))
        
    for _ in range(cnt+1):
        daegi += 1
        lst.append((daegi, 1))

    if bbun >= t:
        print(lst.index((t, bd)) % a)
        break
        