n = 1
 
while True:
    a = input()
    b = input()
    
    if a == "END" and b == "END":
        break
    else:
        a = sorted(list(a))
        b = sorted(list(b))
        
        if a == b:
            print("Case", str(n)+ ": same")
        elif a != b:
            print("Case", str(n)+ ": different")
            
        n += 1
        