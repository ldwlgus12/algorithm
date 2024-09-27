t = int(input())

for i in range(t):
    n = input()
    Sum = str(int(n) + int(n[::-1]))
    
    if Sum == Sum[::-1]:
        print("YES")
    else:
        print("NO")