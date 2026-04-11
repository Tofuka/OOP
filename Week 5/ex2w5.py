class NhanVien:
    LUONG_CO_SO = 2_000_000 

    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.luong_toi_da = luong_toi_da
        self.he_so_luong = he_so_luong 

    @property
    def he_so_luong(self):
        return self._he_so_luong

    @he_so_luong.setter
    def he_so_luong(self, gia_tri):
        if gia_tri > 0:
            self._he_so_luong = gia_tri
        else:
            raise ValueError(f"Lỗi: Hệ số lương của {self.ma_nv} phải lớn hơn 0!")

    def tinh_thu_nhap(self):
        thu_nhap = self.he_so_luong * self.LUONG_CO_SO
        return min(thu_nhap, self.luong_toi_da)
        
    # Phương thức mặc định cho lớp cha
    def lay_vai_tro(self):
        return "Nhân viên chung"


class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_lao_dong):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap_lao_dong = phu_cap_lao_dong

    def tinh_thu_nhap(self):
        luong_cb = super().tinh_thu_nhap() 
        tong_luong = luong_cb + self.phu_cap_lao_dong
        return min(tong_luong, self.luong_toi_da)

    def lay_vai_tro(self):
        return f"CTV ({self.thoi_han_hd})"


class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri_cv):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri_cv = vi_tri_cv

    def lay_vai_tro(self):
        return f"NVCT ({self.vi_tri_cv})"


class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bd_quan_ly, phu_cap_quan_ly):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bd_quan_ly = ngay_bd_quan_ly
        self.phu_cap_quan_ly = phu_cap_quan_ly

    def tinh_thu_nhap(self):
        luong_cb = super().tinh_thu_nhap()
        tong_luong = luong_cb + self.phu_cap_quan_ly
        return min(tong_luong, self.luong_toi_da)

    def lay_vai_tro(self):
        return f"Trưởng Phòng (từ {self.ngay_bd_quan_ly})"



def in_bang_luong(danh_sach_nv):
    header = f"| {'STT':<3} | {'Mã NV':<5} | {'Họ Tên Nhân Viên':<20} | {'Giới Tính':<9} | {'HSL':<4} | {'Vai Trò (Chi tiết)':<30} | {'Thực Lãnh (VNĐ)':>16} |"
    
    print("-" * len(header))
    print(f"| {'BẢNG TỔNG HỢP THU NHẬP NHÂN SỰ':^{len(header) - 4}} |")
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    # Sử dụng enumerate để tự động tạo Số Thứ Tự (bắt đầu từ 1)
    for stt, nv in enumerate(danh_sach_nv, start=1):
        thu_nhap = nv.tinh_thu_nhap()
        # Ép kiểu format: căn trái (<), căn phải (>), định dạng số tiền có dấu phẩy (,.0f), số thập phân (.1f)
        row = f"| {stt:<3} | {nv.ma_nv:<5} | {nv.ho_ten:<20} | {nv.gioi_tinh:<9} | {nv.he_so_luong:<4.1f} | {nv.lay_vai_tro():<30} | {thu_nhap:>16,.0f} |"
        print(row)
        
    print("-" * len(header))

# main
if __name__ == "__main__":
    try:
        phong_ban = [
            CongTacVien("NV01", "Nguyễn Văn A", 2000, "Nam", "Hà Nội", 1.5, 10_000_000, "6 tháng", 1_000_000),
            NhanVienChinhThuc("NV02", "Trần Thị B", 1995, "Nữ", "Hà Nội", 3.0, 20_000_000, "Chuyên viên IT"),
            NhanVienChinhThuc("NV03", "Phạm Văn D", 1998, "Nam", "Hải Phòng", 2.5, 20_000_000, "Tester"),
            TruongPhong("NV04", "Lê Văn C", 1985, "Nam", "Hà Nội", 15.0, 40_000_000, "01/01/2023", 15_000_000)
        ]

        in_bang_luong(phong_ban)

    except ValueError as e:
        print(f"\n[Lỗi Khởi Tạo]: {e}")