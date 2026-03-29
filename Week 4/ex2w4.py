import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class LineSegment:
    def __init__(self, *args):
        self.__d1 = None
        self.__d2 = None

        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
            
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            S = args[0]
            self.__d1 = copy.deepcopy(S.__d1)
            self.__d2 = copy.deepcopy(S.__d2)
            
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
            
        elif len(args) == 4 and all(isinstance(arg, int) for arg in args):
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
            
        else:
            raise ValueError("Tham số truyền vào không hợp lệ!")
        
    def display(self):
        print(f"Đoạn thẳng từ {self.__d1} đến {self.__d2}")

if __name__ == "__main__":
    ls1 = LineSegment()
    print("Mặc định:", end=" ")
    ls1.display()

    p1 = Point(2, 3)
    p2 = Point(4, 5)
    ls2 = LineSegment(p1, p2)
    print("2 Điểm:", end=" ")
    ls2.display()

    ls3 = LineSegment(0, 0, 10, 10)
    print("4 Tọa độ:", end=" ")
    ls3.display()

    ls4 = LineSegment(ls3)
    print("Sao chép:", end=" ")
    ls4.display()