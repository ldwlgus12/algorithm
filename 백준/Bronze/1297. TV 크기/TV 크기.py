d, h, w = map(int, input().split())
 
height =  int((h*d) / (((h**2) + (w**2)) **(1/2)))
width =  int((w*d) / (((h**2) + (w**2)) **(1/2)))

print(height, width)
