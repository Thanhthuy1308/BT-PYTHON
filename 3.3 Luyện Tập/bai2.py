# Bai 2: Kiem tra tam giac

a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Do dai ba canh la tam giac")
else:
    print("Day khong phai do dai ba canh tam giac")