num = int(input())
one = []
zero = []

for i in range(num):
    vote = int(input())
    if vote == 1:
        one.append(i)
    else:
        zero.append(i)

if len(one) > len(zero):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")