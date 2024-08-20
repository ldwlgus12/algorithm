a, b=input().split()

mn = int(a.replace('6', '5')) + int(b.replace('6', '5'))
mx = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(mn, mx)