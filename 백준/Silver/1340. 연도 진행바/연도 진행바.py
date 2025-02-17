time = input().split(' ')

month = time[0]
dd = int(time[1][:-1])
yyyy = int(time[2])
hh, mm = map(int, time[3].split(':'))

month_name = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]         
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if yyyy % 400 == 0 or (yyyy % 4 == 0 and yyyy % 100 != 0):
    month_day[1] += 1

total = sum(month_day)*24*60
month_idx = month_name.index(month)
current = (sum(month_day[:month_idx]) + dd - 1) * 24 * 60 + hh * 60 + mm

print(current/total*100) 
