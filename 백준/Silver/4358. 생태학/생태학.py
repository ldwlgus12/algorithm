import sys
dic = {}
cnt = 0

while True:
    tree = sys.stdin.readline().rstrip()
    
    if tree == '':
        break
    cnt += 1 
    
    if tree in dic: 
        dic[tree] += 1
    else:
        dic[tree] = 1
        
sort_dic = dict(sorted(dic.items()))

for i in sort_dic:
    a = sort_dic[i]
    percent = (a / cnt * 100)    
    print("%s %.4f" %(i, percent))