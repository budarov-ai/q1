sec = int(input('Hey, how much second to the moon? :'))
#import datetime
#date_form = str(datetime.timedelta(seconds=sec))
#print(date_form)

hh = sec // 3600
mm = hh // 60
ss = mm // 60
print('{:d}:{:02d}:{:02d}'.format(hh, mm, ss))
