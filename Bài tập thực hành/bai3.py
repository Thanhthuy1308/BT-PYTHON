# B3: Tạo file
with open("demo_file1.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO\n")

# a) In nội dung file trên một dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("In trên một dòng:")
    print(content.replace("\n", " "))

# b) In theo từng dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("In từng dòng:")
    for line in f:
        print(line.strip())