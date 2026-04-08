import math

class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        """Khởi tạo phân số với tử số và mẫu số (mặc định mẫu = 1)"""
        if mau_so == 0:
            raise ValueError("Lỗi: Mẫu số không được bằng 0.")
        
        self.tu_so = tu_so
        self.mau_so = mau_so
        # Tự động tối giản phân số ngay khi khởi tạo (tùy chọn)
        self.toi_gian()

    def toi_gian(self):
        """Rút gọn phân số về dạng tối giản"""
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
        # Đảm bảo dấu trừ nằm ở tử số nếu là số âm
        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so
        return self

    def tong(self, other):
        """Cộng hai phân số: a/b + c/d = (ad + bc) / bd"""
        moi_tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        moi_mau = self.mau_so * other.mau_so
        return PhanSo(moi_tu, moi_mau)

    def hieu(self, other):
        """Trừ hai phân số: a/b - c/d = (ad - bc) / bd"""
        moi_tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        moi_mau = self.mau_so * other.mau_so
        return PhanSo(moi_tu, moi_mau)

    def nhan(self, other):
        """Nhân hai phân số: a/b * c/d = (a*c) / (b*d)"""
        moi_tu = self.tu_so * other.tu_so
        moi_mau = self.mau_so * other.mau_so
        return PhanSo(moi_tu, moi_mau)

    def chia(self, other):
        """Chia hai phân số: a/b : c/d = (a*d) / (b*c)"""
        if other.tu_so == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử số bằng 0.")
        moi_tu = self.tu_so * other.mau_so
        moi_mau = self.mau_so * other.tu_so
        return PhanSo(moi_tu, moi_mau)

    def __str__(self):
        """Định dạng cách hiển thị phân số khi in ra màn hình"""
        if self.mau_so == 1:
            return f"{self.tu_so}"
        return f"{self.tu_so}/{self.mau_so}"

# --- Kiểm tra chương trình ---
try:
    ps1 = PhanSo(1, 2)  # 1/2
    ps2 = PhanSo(3, 4)  # 3/4

    print(f"Phân số 1: {ps1}")
    print(f"Phân số 2: {ps2}")
    
    print(f"Tổng: {ps1.tong(ps2)}")
    print(f"Hiệu: {ps1.hieu(ps2)}")
    print(f"Nhân: {ps1.nhan(ps2)}")
    print(f"Chia: {ps1.chia(ps2)}")

    # Thử trường hợp tối giản
    ps3 = PhanSo(10, 20)
    print(f"Phân số 10/20 tối giản thành: {ps3}")

    # Thử trường hợp mẫu số bằng 0
    # ps_loi = PhanSo(1, 0) 

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)