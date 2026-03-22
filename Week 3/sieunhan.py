class SieuNhan:
    def __init__(self, ten, weapon, color):
        self.ten = ten
        self.weapon = weapon
        self.color = color

    def infomation(self):
        return f"Siêu nhân {self.ten} - Vũ khí: {self.weapon} - Màu: {self.color}"

sieu_nhan_A = SieuNhan("A", "Kiếm", "Đỏ")
sieu_nhan_B = SieuNhan("B", "Khiên", "Xanh")

print(sieu_nhan_A.infomation())
print(sieu_nhan_B.infomation())