n = int(input())
result = 0

for _ in range(n):
    watch, time = input().split()
    h, m = map(int, watch.split(":"))
    now_time = h*60+m

    for i in range(int(time)):
        if now_time >= 420 and now_time < 1140:
            result += 10
            now_time += 1
        else:
            result += 5
            now_time += 1

        if now_time == 1440:
            now_time = 0

print(result)
