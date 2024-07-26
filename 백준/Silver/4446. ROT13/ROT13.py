m = ["a", "i", "y", "e", "o", "u"]
j = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]

while(True):
    try: 
        string = input()        
        result = ""
        
        for i in string:
            s_lower = True
            
            if i.isupper():
                s_lower = False
                i = i.lower()
            
            if (i in m):
                move_char = m[(m.index(i) + 3) % 6]
                result += move_char if s_lower else move_char.upper()
            elif (i in j):
                move_char = j[(j.index(i) + 10) % 20]
                result += move_char if s_lower else move_char.upper()
                
            else:
                result += i                
        print(result)
        
    except:
        break
        