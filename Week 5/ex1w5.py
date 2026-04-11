class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def lay_loai_hang(self):
        return "Chung"

    def lay_chi_tiet(self):
        return ""


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def lay_loai_hang(self):
        return "Điện Máy"

    def lay_chi_tiet(self):
        return f"BH: {self.tg_baohanh} tháng, {self.dien_ap}V, {self.cong_suat}W"


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def lay_loai_hang(self):
        return "Sành Sứ"

    def lay_chi_tiet(self):
        return f"Chất liệu: {self.loai_nguyenlieu}"


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def lay_loai_hang(self):
        return "Thực Phẩm"

    def lay_chi_tiet(self):
        return f"HSD: {self.ngay_sx} -> {self.ngay_hethan}"


def xuat_danh_sach_dang_cot(danh_sach):
    header = f"| {'Mã Hàng':<8} | {'Tên Sản Phẩm':<22} | {'Nhà SX':<15} | {'Giá Bán (VNĐ)':>15} | {'Loại':<12} | {'Thông Tin Đặc Thù':<38} |"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for sp in danh_sach:
        gia_format = f"{sp.gia:,.0f}" 
        row = f"| {sp.ma_hang:<8} | {sp.ten_hang:<22} | {sp.nha_sx:<15} | {gia_format:>15} | {sp.lay_loai_hang():<12} | {sp.lay_chi_tiet():<38} |"
        print(row)
        
    print("-" * len(header))


if __name__ == "__main__":
    kho_hang = [
        HangDienMay("DM001", "Máy lạnh Daikin", "Daikin", 12500000, 24, 220, 1500),
        HangDienMay("DM002", "Tủ lạnh Aqua", "Aqua", 6500000, 12, 220, 180),
        HangSanhSu("SS001", "Bộ ấm trà Bát Tràng", "Bát Tràng", 850000, "Men rạn"),
        HangThucPham("TP001", "Sữa tươi tiệt trùng", "Vinamilk", 35000, "10/04/2026", "10/10/2026")
    ]
    xuat_danh_sach_dang_cot(kho_hang)