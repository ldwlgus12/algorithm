import sys
start, end, stream = sys.stdin.readline().split()

start = int(start[:2] + start[3:])
end = int(end[:2] + end[3:])
stream = int(stream[:2] + stream[3:])

result = set()
cnt = 0

while True:
    try:
        time, name = sys.stdin.readline().split()
        time = int(time[:2] + time[3:])
        
        if time <= start:
            result.add(name)
        elif end <= time <= stream and name in result:
            result.remove(name)
            cnt += 1
    except:
        break

print(cnt)