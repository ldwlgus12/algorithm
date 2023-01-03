A, B = map(int, input().split())

if A > B and 10000 >= A >= -10000 and 10000 >= B >= -10000: 
    print(">")
elif A < B and 10000 >= A >= -10000 and 10000 >= B >= -10000: 
    print("<")
elif A == B and 10000 >= A >= -10000 and 10000 >= B >= -10000: 
    print("==")