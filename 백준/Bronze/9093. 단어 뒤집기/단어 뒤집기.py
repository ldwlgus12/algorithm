T = int(input())
string_list = []
 

for i in range(T):
    string = input().split()
    for j in range(len(string)):
        string[j] = string[j][::-1]
    print(*string)