class ConCho:
    def __init__(self, ten, color, giong, emo):
        self.ten = ten
        self.mau_sac = color
        self.giong = giong
        self.cam_xuc = emo
    def __str__(self):
        return f"Con chó tên {self.ten}, màu {self.mau_sac}, giống {self.giong}, cảm xúc {self.cam_xuc}"
    def bark(self):
        print(f"{self.ten} đang sủa: Gâu gâu!")

    def vayduoi(self):
        print(f"{self.ten} đang vẫy đuôi mừng.")

    def eat(self):
        print(f"{self.ten} đang ăn.")

    def chay(self):
        print(f"{self.ten} đang chạy tung tăng.")

dog1 = ConCho("Độ", "Vàng", "Cao Bằng", "Vui vẻ")
print(dog1)
dog1.bark()
dog1.eat()
dog2 = ConCho("Bull", "Trắng", "Husky", "Bình thường")
print(dog2)
dog2.chay()

class Car:
    def __init__(self, brand, size, color, price):
        self.hang = brand
        self.kich_thuoc = size
        self.mau = color
        self.gia = price

    def tang_toc(self):
        print(f"Xe {self.hang} đang tăng tốc...")

    def giam_toc(self):
        print(f"Xe {self.hang} đang phanh lại.")

    def dam(self):
        print("RẦM! Xe đã va chạm.")
    def no(self):
        print("Nổ xe rồi các cháu ơi!")

mycar = Car("Toyota", "4 chỗ", "Đen", "500 triệu")
mycar.tang_toc()
mycar.no()

class Account:
    def __init__(self, name, number, bank, balance):
        self.ten_tk = name
        self.so_tk = number
        self.ngan_hang = bank
        self.so_du = balance

    def kiem_tra_so_du(self):
        print(f"Số dư hiện tại của {self.ten_tk}: {self.so_du} VNĐ")

    def gui(self, ammount):
        self.so_du += ammount
        print(f"Đã gửi {ammount} vào tài khoản.")

    def rut(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            print(f"Đã rút {so_tien}. Số dư còn lại: {self.so_du}")
        else:
            print("Số dư không đủ để thực hiện giao dịch.")


my_acc = Account("NGUYEN VAN A", "123456", "V-Bank", 1000000)
my_acc.kiem_tra_so_du()
my_acc.rut(200000)