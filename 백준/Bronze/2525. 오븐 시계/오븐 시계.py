A, B = map(int, input().split())
C = int(input())
min = 0
A_hour = 0

hap = B + C
hour = hap//60

if hour >= 1:
    A_hour = A + hour
    if A_hour >= 24:
        A_hour = A_hour%24
        print(A_hour, end=" ")
    else:
       print(A_hour, end=" ")
else:
    print(A, end=" ")

if hap%60 == 0:
    print(0)
else:
    if hap > 60:
        print(hap%60)
    else:
        print(hap)