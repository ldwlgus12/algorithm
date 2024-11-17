for i in range(int(input())):
    a, b = input().split()
    
    if sorted(list(a)) == sorted(list(b)):
        print("%s & %s are anagrams." %(a, b))
    else:
        print("%s & %s are NOT anagrams." %(a, b))
        