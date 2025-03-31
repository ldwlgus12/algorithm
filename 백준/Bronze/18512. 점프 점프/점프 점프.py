x, y, p1, p2 = map(int, input().split())
visit_x, visit_y = [p1], [p2]
result = -1

for i in range(1000):
    visit_x.append(visit_x[i]+x)
    visit_y.append(visit_y[i]+y)
    
    if visit_x[i]+x in visit_y or visit_y[i]+y in visit_x:
        result = min(visit_x[i]+x, visit_y[i]+y)
        break
        
print(result)
