# B2: Ghi văn bản vào file và đọc lại
text = input("Nhập đoạn văn bản: ")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Đọc lại file
with open("output.txt", "r", encoding="utf-8") as f:
    print("Nội dung file:")
    print(f.read())