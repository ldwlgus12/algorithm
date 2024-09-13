h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
total = h2*3600 + m2*60 + s2 - (h1*3600 + m1*60 + s1)

if total < 0:
    total += 60*60*24
    
h = total // 3600 
m = (total % 3600) // 60 
s = total % 60

print("%02d:%02d:%02d" % (h, m, s))
