import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self, ten_diem):
        print(f"Toạ độ điểm {ten_diem}: ({self.x}, {self.y})")

    def range_O(self):
        return math.sqrt(self.x**2 + self.y**2)

    def range(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

a = Point(3, 4)
a.display("A")

xb = int(input("Nhập x điểm B: "))
yb = int(input("Nhập y điểm B: "))
b = Point(xb, yb)
b.display("B")

c = Point(-b.x, -b.y)
c.display("C")

dist_bo = b.range_O()
print(f"d(B, O)= {dist_bo:.2f}")

dist_ab = a.range(b)
print(f"d(A, B)= {dist_ab:.2f}")