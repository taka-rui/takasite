import datetime
today = datetime.date.today()
birhtday = datetime.date(1999,11,17)
life = today - birhtday
print(life.days)