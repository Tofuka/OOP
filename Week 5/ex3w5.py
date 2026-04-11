class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def gioi_tinh(self):
        return self._gioi_tinh

    @gioi_tinh.setter
    def gioi_tinh(self, gia_tri):
        gt_chuan = gia_tri.strip().lower()
        if gt_chuan in ["nam", "nữ", "nu", "khác", "khac"]:
            self._gioi_tinh = gia_tri.capitalize()
        else:
            self._gioi_tinh = "Khác"

    def lay_vai_tro(self):
        return "Cán Bộ"

    def lay_thong_tin_rieng(self):
        return ""


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac 

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, gia_tri):
        if 1 <= int(gia_tri) <= 10:
            self._bac = int(gia_tri)
        else:
            raise ValueError(f"Lỗi: Bậc của công nhân phải từ 1 đến 10.")

    def lay_vai_tro(self):
        return "Công Nhân"

    def lay_thong_tin_rieng(self):
        return f"Bậc: {self.bac}/10"


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def lay_vai_tro(self):
        return "Kỹ Sư"

    def lay_thong_tin_rieng(self):
        return f"Ngành: {self.nganh_dao_tao}"


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def lay_vai_tro(self):
        return "Nhân Viên"

    def lay_thong_tin_rieng(self):
        return f"Công việc: {self.cong_viec}"
    
# Class QLCB

class QLCB:
    def __init__(self):
        self.danh_sach_cb = []

    def them_can_bo(self, can_bo):
        self.danh_sach_cb.append(can_bo)
        print(f"[*] Đã thêm thành công: {can_bo.ho_ten} ({can_bo.lay_vai_tro()})")

    def tim_kiem_theo_ten(self, tu_khoa):
        # Lọc danh sách không phân biệt hoa thường
        ket_qua = [cb for cb in self.danh_sach_cb if tu_khoa.lower() in cb.ho_ten.lower()]
        return ket_qua

    def hien_thi_danh_sach(self, danh_sach=None):
        ds_can_in = danh_sach if danh_sach is not None else self.danh_sach_cb
        
        if not ds_can_in:
            print("\n[!] Danh sách trống.")
            return

        header = f"| {'STT':<3} | {'Họ Tên':<20} | {'Tuổi':<4} | {'Giới Tính':<9} | {'Địa Chỉ':<15} | {'Vai Trò':<12} | {'Thông Tin Đặc Thù':<30} |"
        print("\n" + "-" * len(header))
        print(header)
        print("-" * len(header))

        for stt, cb in enumerate(ds_can_in, start=1):
            row = f"| {stt:<3} | {cb.ho_ten:<20} | {cb.tuoi:<4} | {cb.gioi_tinh:<9} | {cb.dia_chi:<15} | {cb.lay_vai_tro():<12} | {cb.lay_thong_tin_rieng():<30} |"
            print(row)
            
        print("-" * len(header) + "\n")


# CHƯƠNG TRÌNH CHÍNH (MENU)

if __name__ == "__main__":
    quan_ly = QLCB()

    # Thêm sẵn một vài dữ liệu mẫu để test
    quan_ly.them_can_bo(KySu("Nguyễn Văn A", 28, "Nam", "Hà Nội", "CNTT"))
    quan_ly.them_can_bo(CongNhan("Trần Thị B", 35, "Nữ", "Hải Phòng", 5))
    quan_ly.them_can_bo(NhanVien("Lê Văn C", 24, "Nam", "Đà Nẵng", "Lễ tân"))

    while True:
        print("\n" + "="*40)
        print(" CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ ".center(40, "="))
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm theo họ tên")
        print("3. Hiển thị thông tin danh sách")
        print("4. Thoát khỏi chương trình")
        print("="*40)
        
        chon = input("Nhập lựa chọn của bạn (1-4): ")

        if chon == '1':
            print("\n--- THÊM CÁN BỘ MỚI ---")
            loai = input("Chọn loại (1-Công Nhân, 2-Kỹ Sư, 3-Nhân Viên): ")
            ten = input("Nhập họ tên: ")
            tuoi = int(input("Nhập tuổi: "))
            gt = input("Nhập giới tính (Nam/Nữ/Khác): ")
            dc = input("Nhập địa chỉ: ")

            try:
                if loai == '1':
                    bac = int(input("Nhập bậc (1-10): "))
                    cb_moi = CongNhan(ten, tuoi, gt, dc, bac)
                elif loai == '2':
                    nganh = input("Nhập ngành đào tạo: ")
                    cb_moi = KySu(ten, tuoi, gt, dc, nganh)
                elif loai == '3':
                    cv = input("Nhập công việc: ")
                    cb_moi = NhanVien(ten, tuoi, gt, dc, cv)
                else:
                    print("Lựa chọn không hợp lệ!")
                    continue
                
                quan_ly.them_can_bo(cb_moi)
            except ValueError as e:
                print(f"[!] Dữ liệu nhập không hợp lệ: {e}")

        elif chon == '2':
            tu_khoa = input("\nNhập tên cán bộ cần tìm: ")
            kq = quan_ly.tim_kiem_theo_ten(tu_khoa)
            print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{tu_khoa}' ---")
            quan_ly.hien_thi_danh_sach(kq)

        elif chon == '3':
            print("\n--- DANH SÁCH TOÀN BỘ CÁN BỘ ---")
            quan_ly.hien_thi_danh_sach()

        elif chon == '4':
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("[!] Lựa chọn không hợp lệ, vui lòng thử lại.")