import math

class Point:
    """Đại diện cho một điểm trong không gian 2D."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Rectangle:
    """Đại diện cho một hình chữ nhật."""
    def __init__(self, width=0, height=0, corner=None):
        self.width = width
        self.height = height
        self.corner = corner if corner else Point(0, 0)

class Circle:
    """Đại diện cho một hình tròn."""
    def __init__(self, center=None, radius=0):
        self.center = center if center else Point(0, 0)
        self.radius = radius

    def point_in_circle(self, point):
        """Kiểm tra một điểm có nằm trong hoặc trên biên hình tròn không."""
        dist = math.sqrt((self.center.x - point.x)**2 + (self.center.y - point.y)**2)
        return dist <= self.radius

    def rect_in_circle(self, rect):
        """Kiểm tra hình chữ nhật có nằm hoàn toàn trong hình tròn không."""
        p = rect.corner
        corners = [
            Point(p.x, p.y),                         # Dưới trái
            Point(p.x + rect.width, p.y),            # Dưới phải
            Point(p.x, p.y + rect.height),           # Trên trái
            Point(p.x + rect.width, p.y + rect.height) # Trên phải
        ]
        for corner in corners:
            if not self.point_in_circle(corner):
                return False
        return True

    def rect_circle_overlap(self, rect):
        """Kiểm tra nếu có bất kỳ góc nào của HCN nằm trong hình tròn."""
        p = rect.corner
        corners = [
            Point(p.x, p.y),
            Point(p.x + rect.width, p.y),
            Point(p.x, p.y + rect.height),
            Point(p.x + rect.width, p.y + rect.height)
        ]
        
        for corner in corners:
            if self.point_in_circle(corner):
                return True
        return False


if __name__ == "__main__":
    center_point = Point(150, 100)
    my_circle = Circle(center_point, 75)

    print(f"--- Thông tin hình tròn ---")
    print(f"Tâm: {my_circle.center}, Bán kính: {my_circle.radius}")
    print("-" * 30)

    test_point = Point(160, 110)
    result_p = my_circle.point_in_circle(test_point)
    print(f"Điểm {test_point} có nằm trong hình tròn? {result_p}")

    inner_rect = Rectangle(20, 20, Point(140, 90))
    result_r1 = my_circle.rect_in_circle(inner_rect)
    print(f"HCN (140,90, 20x20) nằm hoàn toàn trong? {result_r1}")

    overlap_rect = Rectangle(100, 100, Point(100, 100))
    result_r2 = my_circle.rect_circle_overlap(overlap_rect)
    print(f"HCN (100,100, 100x100) có chồng lấn không? {result_r2}")