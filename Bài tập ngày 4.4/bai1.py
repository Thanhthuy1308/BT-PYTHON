_tuple = ('a', 'b', 'd', 'e')

# Chuyển tuple sang list để có thể chỉnh sửa
temp_list = list(_tuple)

# Thêm 'c' vào vị trí số 2 (index bắt đầu từ 0)
temp_list.insert(2, 'c')

# Chuyển lại thành tuple
_new_tuple = tuple(temp_list)

print(f"Bài 1: {_new_tuple}")