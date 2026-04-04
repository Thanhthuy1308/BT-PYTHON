lst = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

# Cách 1: Loại bỏ hoàn toàn phần tử trùng
new1 = []
for x in lst:
    if lst.count(x) == 1:
        new1.append(x)

print("Kết quả cách 1:", new1)


# Cách 2: Giữ lại 1 phần tử (loại trùng)
new2 = []
for x in lst:
    if x not in new2:
        new2.append(x)

print("Kết quả cách 2:", new2)