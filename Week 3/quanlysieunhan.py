class SieuNhan:
    def __init__(self, ten, power,weapon):
        self.ten = ten
        self.suc_manh = power
        self.weapon = weapon

list_sn = []

while True:
    print("\n--- Nhập danh sách siêu nhân(ghi empty để thoát) ---")
    ten = input("Tên siêu nhân: ")
    if ten.lower() == 'empty':
        break
    power = input("Nhập sức mạnh: ")
    weapon = input("Nhập vũ khí: ")

    sn = SieuNhan(ten, power,weapon)
    list_sn.append(sn)

print("\n--- Danh sách siêu nhân ---")

for item in list_sn:
    print(f"Tên: {item.ten} | Sức mạnh: {item.suc_manh} | Vũ khí: {item.weapon}")