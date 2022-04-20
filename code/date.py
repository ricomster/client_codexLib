from datetime import date
from datetime import datetime, timedelta

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

d5 = today.strftime("%Y-%m-%d")
print("d5 =", d5)

d6 = today.strftime("%Y%m%d")

now = datetime.now()
td = timedelta(days=7)
# your calculated date
my_date = now + td

current = now.strftime("%Y-%m-%d")
next_week = my_date.strftime("%Y-%m-%d")

print(current, "+7 jadi", next_week)

# td = timedelta(days=4)
# pengembalian = d6+td
# print ("tanggal pengem = ", pengembalian)