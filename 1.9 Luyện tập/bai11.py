# Giả sử list cho trước
danh_sach = ["Python", "Hoc", "Lap", "Trinh", "AI", "Code"]

# Nhập số n từ bàn phím
n = int(input("Nhập vào độ dài n: "))

# Tìm các từ thỏa mãn điều kiện
ket_qua = []
for tu in danh_sach:
    if len(tu) > n:
        ket_qua.append(tu)

print(f"Các từ có độ dài lớn hơn {n} là: {ket_qua}")