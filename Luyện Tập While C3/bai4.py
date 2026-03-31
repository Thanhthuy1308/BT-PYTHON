n = int(input("Nhập n: "))

tong = 0
for i in range(0, n):
    if i % 2 == 0:
        tong += i

print("Tổng các số chẵn nhỏ hơn", n, "là:", tong)