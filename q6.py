start = int(input('how much? :'))
finish = int(input('how much? :'))
day = 1
day_range = start + (day / 100 * 10)
while day_range <= 3:
    day += 1
    day_range += start
    print(f'eshe ne dobejal :( %.d' % day_range)






