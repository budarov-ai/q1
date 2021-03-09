import status

start = int(input('how much? :'))
finish = int(input('how much? :'))
day = 1
day_range = start + (day / 100 * 10)
while day_range <= finish:
    day += 1
    day_range *= 1.1
#status  = '+' if day_range > finish else '-'
#print(f'ok:{status} %.d' % day_range)
    print(day, f'eshe ne dobejal :( %.d' % day_range)
    if day_range >=finish:
        print("условие выполнено :", day_range)







