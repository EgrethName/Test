import datetime

year, month, day = [int(i) for i in input().split()]
days_number = int(input())
data = datetime.date(year, month, day)
datadelta = datetime.timedelta(days=days_number)
data_mid = str(data + datadelta).split("-")
data_out = [int(i) for i in data_mid]
print(*data_out)
