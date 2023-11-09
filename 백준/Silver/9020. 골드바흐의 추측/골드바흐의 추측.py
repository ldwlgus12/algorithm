def gold(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

t = int(input())

for i in range(t): 
    n = int(input())
    a = n//2
    
    while a > 0:
        if gold(a):
            if gold(n - a):
                print(a, n-a)
                break
        a -= 1
        