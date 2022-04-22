from datetime import datetime, timedelta

x = '2017-05-15'
res = (datetime.strptime(x, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')

print(res) 