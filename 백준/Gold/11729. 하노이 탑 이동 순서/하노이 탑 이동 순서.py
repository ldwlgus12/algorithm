def top(n, first, third):
    if n == 1:
        print(first, third)
        return
       
    top(n-1, first, 6-first-third)
    print(first, third)
    top(n-1, 6-first-third, third)
    
n = int(input())

print(2**n-1)
top(n, 1, 3)
