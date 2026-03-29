class NhanVien:
    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong, luong_max):
        self.__tenNhanVien = ten_nhan_vien
        self.__luongCoBan = luong_co_ban
        self.__heSoLuong = he_so_luong
        self.LUONG_MAX = luong_max

    def get_tenNhanVien(self):
        return self.__tenNhanVien

    def set_tenNhanVien(self, ten):
        self.__tenNhanVien = ten

    def get_luongCoBan(self):
        return self.__luongCoBan

    def set_luongCoBan(self, luong):
        self.__luongCoBan = luong

    def get_heSoLuong(self):
        return self.__heSoLuong

    def set_heSoLuong(self, he_so):
        self.__heSoLuong = he_so

    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    def inTTin(self):
        print("\n--- Thông Tin Nhân Viên ---")
        print(f"Tên nhân viên: {self.__tenNhanVien}")
        print(f"Lương cơ bản: {self.__luongCoBan:,.0f} VNĐ")
        print(f"Hệ số lương: {self.__heSoLuong}")
        print(f"Lương hiện tại: {self.tinhLuong():,.0f} VNĐ")
        print("---------------------------")

    def tangLuong(self, muc_tang):
        he_so_luong_moi = self.__heSoLuong + muc_tang
        luong_kien_nghi = self.__luongCoBan * he_so_luong_moi

        if luong_kien_nghi > self.LUONG_MAX:
            print(f"=> THÔNG BÁO: Không thể tăng lương cho {self.__tenNhanVien}!")
            print(f"   Lương đề xuất ({luong_kien_nghi:,.0f}) vượt quá lương tối đa ({self.LUONG_MAX:,.0f}).")
            return False
        else:
            self.__heSoLuong = he_so_luong_moi
            return True

if __name__ == "__main__":
    nv1 = NhanVien("Nguyễn Văn A", 5000000, 2.0, 15000000)
    nv1.inTTin()

    print("\nLần 1: Thử tăng hệ số lương thêm 0.5...")
    if nv1.tangLuong(0.5):
        print("-> Tăng lương thành công!")

    print("\nLần 2: Thử tăng hệ số lương thêm 1.0...")
    if nv1.tangLuong(1.0):
        print("-> Tăng lương thành công!")
    nv1.inTTin()