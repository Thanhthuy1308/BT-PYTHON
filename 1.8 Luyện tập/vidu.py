
cipher_map = {'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%', ' ': ' '}


decipher_map = {v: k for k, v in cipher_map.items()}

def encrypt(text):
    """Hàm mã hóa văn bản"""
    result = ""
    for char in text.lower():
        
        result += cipher_map.get(char, char)
    return result

def decrypt(encoded_text):
    """Hàm giải mã văn bản"""
    result = ""
    for char in encoded_text:
  
        result += decipher_map.get(char, char)
    return result


original_text = "abc d"
encoded = encrypt(original_text)
decoded = decrypt(encoded)

print(f"Văn bản gốc: {original_text}")
print(f"Sau khi mã hóa: {encoded}")
print(f"Sau khi giải mã: {decoded}")