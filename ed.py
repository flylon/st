def encrypt_text_to_binary(input_file_path, output_file_path, key=42):
    """讀取文字檔，加密後寫入二進制檔"""
    # 以讀取模式開啟文字檔
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 將文字轉成位元組 (bytes)
    data_bytes = text.encode('utf-8')
    
    # 使用 XOR 對每個位元組進行加密
    encrypted_bytes = bytearray(b ^ key for b in data_bytes)
    
    # 寫入二進制檔案
    with open(output_file_path, 'wb') as f:
        f.write(encrypted_bytes)
    print(f"加密完成，已輸出至：{output_file_path}")

def decrypt_binary_to_text(input_file_path, output_file_path, key=42):
    """讀取二進制加密檔，解密後還原成文字檔"""
    # 讀取二進制檔案
    with open(input_file_path, 'rb') as f:
        encrypted_bytes = f.read()
    
    # 使用相同的 XOR 金鑰進行解密
    decrypted_bytes = bytearray(b ^ key for b in encrypted_bytes)
    
    # 將位元組轉回字串
    text = decrypted_bytes.decode('utf-8')
    
    # 寫入還原的文字檔
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"解密完成，已輸出至：{output_file_path}")


# 1. 加密：將 original.txt 加密成 encrypted.bin (金鑰設為 123)
#encrypt_text_to_binary('/content/stock_word03.py', '/content/03.txt', 123456787654321)

# 2. 解密：將 encrypted.bin 還原成 decrypted.txt
#decrypt_binary_to_text('/content/03.txt', '/content/stock_word03.txt', 123456787654321)