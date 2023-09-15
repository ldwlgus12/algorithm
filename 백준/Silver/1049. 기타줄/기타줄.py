n, m = map(int, input().split())
package = []
one = []

for i in range(m):
    a, b = map(int, input().split())
    package.append(a)
    one.append(b)

min_package = min(package)
result = 0

while n > 0:
    if n >= 6:
        min_one = min(one)*6
        n -= 6
    else:
        min_one = min(one)*n
        n -= n
        
    if min_one < min_package:
        result += min_one
    else:
        result += min_package

print(result)
