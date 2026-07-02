time = '1h 45m,360s,25m,30m 120s,2h 60s'

items = time.replace(',', ' ').split()

sum_seconds = 0

for item in items:
    if 'h' in item:
        sum_seconds += int(item.replace('h', '')) * 3600
    elif 'm' in item:
        sum_seconds += int(item.replace('m', '')) * 60
    elif 's' in item:
        sum_seconds += int(item.replace('s', ''))

minutes = sum_seconds // 60

print("Всего:", minutes, "минут")
