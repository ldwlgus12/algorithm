for i in range(int(input())):
    alpah = [0 for _ in range(26)] 
    words = input()
    words = list(words)

    for j in words:
        if ord(j) >= 97 and ord(j) <= 122:
            alpah[ord(j)-97] += 1
        elif ord(j) >= 65 and ord(j) <= 90: 
            alpah[ord(j)-65] += 1
        else:
            continue
            
    print(f'Case {i+1}:', end=' ')
    
    if min(alpah) == 0:
        print("Not a pangram")
    elif min(alpah) == 1:
        print("Pangram!")
    elif min(alpah) == 2:
        print("Double pangram!!")
    elif min(alpah) == 3:
        print("Triple pangram!!!")
        