# Bai 3: Tinh tuoi tu nam sinh

import time

nam_sinh = int(input("Nhap nam sinh: "))

x = time.localtime()
nam_hien_tai = x[0]

tuoi = nam_hien_tai - nam_sinh

print("Nam sinh", nam_sinh, ", vay ban", tuoi, "tuoi")