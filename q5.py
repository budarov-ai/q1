profit = int(input('сколько заработано? :'))
lost = int(input('сколько потрачено? :'))
emp = int(input('сколько у вас сотрудников? :'))

if profit > lost:
    print('вы в плюсе!', profit - lost)
    print('каждый сотрудник принес Вам :', (profit - lost) / emp)
elif profit < lost:
    print('вы теряете деньги', profit - lost)
