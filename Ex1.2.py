seconds = 42*60 + 42
miles = 10 / 1.61
hours = seconds / 3600
speed = miles / hours

pace_seconds = seconds / miles
pace_minutes = int(pace_seconds // 60)
pace_remain = pace_seconds % 60

print("Seconds:", seconds)
print("Miles:", f"{miles:.2f}")
print("Speed (mph):", f"{speed:.2f}")
print("Pace:", pace_minutes,"m", f"{pace_remain:.2f}","s per mile")