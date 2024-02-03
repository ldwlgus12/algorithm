a, b = map(int, input().split(':'))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = gcd(max(a, b), min(a, b))
print(f"{a//t}:{b//t}")