# B5: Đếm số lần xuất hiện từ
with open("demo_file2.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
count_dict = {}

for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

print(count_dict)