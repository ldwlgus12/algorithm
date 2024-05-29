import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    record = list(map(str, input().split()))

    while True:
        animal = list(map(str, input().split()))

        if animal[0] == "what":
            print(" ".join(record))
            break

        while animal[2] in record:
            record.remove(animal[2])
            