
from datetime import date
now = date.today()
birthday = date(1964, 7, 31)
diff = now - birthday
print(type(diff))
