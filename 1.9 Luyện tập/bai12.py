# List đầu vào theo ví dụ
_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

# Nhập giá trị độ dài tối thiểu từ bàn phím
n = int(input("Nhập độ dài tối thiểu: "))

dem = 0
for chuoi in _list:
    # Kiểm tra 2 điều kiện cùng lúc dùng 'and'
    if len(chuoi) >= n and chuoi[0] == chuoi[-1]:
        dem += 1
        print(f"Thỏa mãn: {chuoi}") # In ra để bạn dễ kiểm tra

print(f"Số lượng chuỗi thỏa mãn điều kiện là: {dem}")