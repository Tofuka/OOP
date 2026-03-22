import math

V = (4/3)*math.pi*5**3
print(f"{V:.2f}")

M = 60*24.95*0.6 + 3 + 59*0.75
print(f"{M:.2f}")

run = (8*60+15)*2 + (7*60+12)*3
start = 6*3600 + 52*60
finish = start + run
print(f"{finish//3600:02}:{(finish%3600)//60:02}:{finish%60:02}")