s = list(input())

zero = s.count('0') // 2
one = s.count('1') // 2

for i in range(zero):
    s.pop(-s[::-1].index('0') - 1)
    
for i in range(one):
    s.pop(s.index('1'))
    
print(''.join(s))
