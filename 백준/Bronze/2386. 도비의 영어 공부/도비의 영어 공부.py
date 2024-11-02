while True :
    n = input()
    
    if n == '#':
        break
        
    low = n[0]
    s = n[2::]
    result = s.count(low) + s.count(low.upper())
    
    print(low, result)
    