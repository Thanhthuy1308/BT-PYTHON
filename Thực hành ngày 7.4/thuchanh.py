class HocVien:

    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop


    def show_info(self):
        info = (f"Họ tên: {self.ho_ten}\n"
                f"Ngày sinh: {self.ngay_sinh}\n"
                f"Email: {self.email}\n"
                f"Điện thoại: {self.dien_thoai}\n"
                f"Địa chỉ: {self.dia_chi}\n"
                f"Lớp: {self.lop}")
        return info


    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop
        print("--- Cập nhật thông tin thành công ---")


if __name__ == "__main__":

    student = HocVien(
        ho_ten="Vu Thi Thanh Thuy",
        ngay_sinh="13/08/2005",
        email="Tv994095@@gmail.com",
        dien_thoai="0392548316",
        dia_chi="Thai Binh",
        lop="IT14.4"
    )

    print("Thông tin ban đầu:")
    print(student.show_info())

    print("\nThay đổi thông tin (sử dụng giá trị mặc định):")
    student.change_info() 
    
    print(student.show_info())

    print("\nThay đổi thông tin (truyền tham số mới):")
    student.change_info(dia_chi="TP. Hồ Chí Minh", lop="IT15.PRO")
    print(student.show_info())