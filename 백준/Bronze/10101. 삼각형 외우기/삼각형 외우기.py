sam = []

for i in range(3):
    num = int(input())
    sam.append(num)

if sam[0] == 60 and sam[1] == 60 and sam[2] == 60:
    print('Equilateral')
elif sum(sam) == 180:
    if sam[0] == sam[1] or sam[1] == sam[2] or sam[0] == sam[2]:
        print('Isosceles')
    else: #sam[0] != sam[1] != sam[2]:
        print("Scalene")
elif sum(sam) != 180:
    print('Error')