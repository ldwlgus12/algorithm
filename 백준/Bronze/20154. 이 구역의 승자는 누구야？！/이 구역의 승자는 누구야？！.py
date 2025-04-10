alpha = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
s = input()
lst = []

for i in s:
    idx = ord(i) - ord('A')
    lst.append(alpha[idx])

result = sum(lst) % 10
if result % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")
    