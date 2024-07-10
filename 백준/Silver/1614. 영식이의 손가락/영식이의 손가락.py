import sys
input = sys.stdin.readline

finger = int(input())
cnt = int(input())
result = 0

if finger == 1:
    if cnt == 0:
        result += finger-1
    else:
        result += 8*cnt
        
elif finger == 5:
    if cnt == 0:
        result += finger-1
    else:
        result += 4 + 8*(cnt)

else:
    if cnt == 0:
        result += finger-1
    else:
        result += 4*(cnt) + 1
        if cnt % 2 == 0:
            result += finger-2
        else:
            result += 4-finger

print(result)
    