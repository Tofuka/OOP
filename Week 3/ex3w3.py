class NhanVien:
    LUONG_MAX = 50000000.0  

    def __init__(self, ten, basesalary, he_so):
        self._tenNhanVien = ten
        self._luongCoBan = basesalary
        self._heSoLuong = he_so

    @property
    def tenNhanVien(self):
        return self._tenNhanVien

    @tenNhanVien.setter
    def tenNhanVien(self, value):
        if value.strip():
            self._tenNhanVien = value
        else:
            print("Lỗi: Tên nhân viên không được để trống!")

    @property
    def luongCoBan(self):
        return self._luongCoBan

    @luongCoBan.setter
    def luongCoBan(self, value):
        if value >= 0:
            self._luongCoBan = value
        else:
            print("Lỗi: Lương cơ bản không thể là số âm!")

    @property
    def heSoLuong(self):
        return self._heSoLuong

    @heSoLuong.setter
    def heSoLuong(self, value):
        if value > 0:
            self._heSoLuong = value
        else:
            print("Lỗi: Hệ số lương phải lớn hơn 0!")

    def tinhLuong(self):
        return self._luongCoBan * self._heSoLuong

    def tangLuong(self, rate):
        luong_moi = self._luongCoBan * (self._heSoLuong + rate)
        
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"!!! Cảnh báo: Lương mới ({luong_moi:,.0f}) vượt ngưỡng tối đa cho phép.")
            return False
        else:
            self._heSoLuong += rate
            return True

    def inTTIn(self):
        """Hiển thị đầy đủ thông tin nhân viên."""
        print("\n" + "="*40)
        print(f"THÔNG TIN NHÂN VIÊN")
        print(f"Họ tên: {self._tenNhanVien}")
        print(f"Lương cơ bản: {self._luongCoBan:,.0f} VND")
        print(f"Hệ số lương: {self._heSoLuong:.2f}")
        print(f"Tổng lương thực nhận: {self.tinhLuong():,.0f} VND")
        print("="*40)

if __name__ == "__main__":
    nv1 = NhanVien("Nguyễn Văn A", 4000000, 2.5) 
    nv1.inTTIn()

    print("\n> Thực hiện tăng thêm 1.5 hệ số lương...")
    if nv1.tangLuong(1.5):
        print("Trạng thái: True")
    nv1.inTTIn()

    print("\n> Thực hiện tăng thêm 15.0 hệ số lương...")
    if not nv1.tangLuong(15.0):
        print("Trạng thái: False")