import math

def tong_2_so(a, b):
    return a + b

def tong_danh_sach(lst):
    return sum(lst)

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tim_nguyen_to(a, b):
    kq = []
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            kq.append(i)
    return kq

def la_so_hoan_hao(n):
    if n < 2:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

def tim_so_hoan_hao(a, b):
    kq = []
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            kq.append(i)
    return kq

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tinh tong 2 so")
        print("2. Tinh tong danh sach")
        print("3. Kiem tra so nguyen to")
        print("4. Tim so nguyen to trong [a, b]")
        print("5. Kiem tra so hoan hao")
        print("6. Tim so hoan hao trong [a, b]")
        print("0. Thoat")

        chon = int(input("Chon chuc nang: "))

        if chon == 1:
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            print("Ket qua:", tong_2_so(a, b))

        elif chon == 2:
            lst = list(map(int, input("Nhap cac so: ").split()))
            print("Tong:", tong_danh_sach(lst))

        elif chon == 3:
            n = int(input("Nhap n: "))
            if la_so_nguyen_to(n):
                print(n, "la so nguyen to")
            else:
                print(n, "khong phai so nguyen to")

        elif chon == 4:
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            print("Cac so nguyen to:", tim_nguyen_to(a, b))

        elif chon == 5:
            n = int(input("Nhap n: "))
            if la_so_hoan_hao(n):
                print(n, "la so hoan hao")
            else:
                print(n, "khong phai so hoan hao")

        elif chon == 6:
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            print("Cac so hoan hao:", tim_so_hoan_hao(a, b))

        elif chon == 0:
            print("Thoat chuong trinh!")
            break

        else:
            print("Chon sai, nhap lai!")

menu()