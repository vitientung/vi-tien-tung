print("\n" + "="*20 + " BÀI 4 " + "="*20)

print("--- 4.2 & 4.3: Xử lý chuỗi ---")
s = input("Nhập chuỗi bất kỳ: ")
print(f"Bỏ khoảng trắng: {s.replace(' ', '').replace(chr(9), '')}")
print(f"In hoa: {s.upper()}")

print("\n--- 4.5: Đảo ngược danh sách từ ---")
ds_tu = input("Nhập danh sách từ (cách nhau bởi dấu cách): ").split()
print("Kết quả:", " ".join(ds_tu[::-1]))

print("\n--- 4.6: Tách họ tên ---")
ho_ten = input("Nhập họ tên đầy đủ: ").strip()
parts = ho_ten.split()
print(f"Họ lót: {' '.join(parts[:-1])}")
print(f"Tên: {parts[-1]}")

print("\n--- 4.7: Loại bỏ chữ số ---")
s_so = input("Nhập chuỗi chứa số: ")
print("Kết quả:", "".join([c for c in s_so if not c.isdigit()]))

print("\n--- 4.8: Tìm từ dài nhất ---")
text = input("Nhập câu tiếng Anh: ").split()
if text:
    max_len = len(max(text, key=len))
    print("Từ dài nhất:", [w for w in text if len(w) == max_len])

