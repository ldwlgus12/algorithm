k = input()

if len(k) <= 2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    seq = True
    a = int(k[0]) - int(k[1])
    
    for i in range(1, len(k)-1):
        if int(k[i]) - int(k[i+1]) != a:
            seq = False
            
    if seq == True:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    else:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
    