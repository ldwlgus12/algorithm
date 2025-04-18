s = list(str(input()))
korea = ['K', 'O', 'R', 'E', 'A']
yonsei = ['Y', 'O', 'N', 'S', 'E', 'I']

for i in s:
    if i == korea[0]:
        korea.remove(i)
        if len(korea) == 0:
            print("KOREA")
            break
            
    if i == yonsei[0]:
        yonsei.remove(i)
        if len(yonsei) == 0:
            print("YONSEI")
            break
            