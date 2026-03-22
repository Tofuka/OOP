def draw_grid(n):
    line = "+ - - - - " * n + "+"
    space = "|         " * n + "|"

    for i in range(n):
        print(line)
        for j in range(4):
            print(space)
    print(line)

draw_grid(2)
print()

draw_grid(4)
print()

draw_grid(6)
print()

draw_grid(10)
print()