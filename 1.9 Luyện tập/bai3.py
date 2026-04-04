_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []
odd_list = []

for so in _list:
    if so % 2 == 0:
        even_list.append(so)
    else:
        odd_list.append(so)

print(f"List số chẵn: {even_list}")
print(f"List số lẻ: {odd_list}")