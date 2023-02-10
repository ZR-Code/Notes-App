import time
y = "Y"
m = "m"
d = "d"
date = time.strftime("%" + y + "/%" + m + "/%" + d)
print(date)