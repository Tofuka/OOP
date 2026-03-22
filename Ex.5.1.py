import time

t = int(time.time())

days = t // 86400
hours = (t % 86400) // 3600
minutes = (t % 3600) // 60
seconds = t % 60

print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")