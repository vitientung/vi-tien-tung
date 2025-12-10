import shutil

# file mẫu để test
try:
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write("Xin chao Python\nDong thu hai\nlongestwordhere")
    print("Đã tạo file test.txt")
except Exception as e:
    print(f"Lỗi tạo file: {e}")

# Bài 7.3: Đọc toàn bộ
print("\n--- 7.3: Đọc file ---")
try:
    with open('test.txt') as f: print(f.read())
except FileNotFoundError:
    print("Không tìm thấy test.txt")

# Bài 7.7: Đếm dòng
print("\n--- 7.7: Đếm số dòng ---")
try:
    print(len(open('test.txt').readlines()))
except: pass

# Bài 7.8: Ghi list vào file
print("\n--- 7.8: Ghi list vào file ---")
lst = ["Cam", "Tao", "Xoai"]
with open('hoaqua.txt', 'w') as f:
    for x in lst: f.write(x + '\n')
print("Đã ghi vào file hoaqua.txt")

# Bài 7.9: Copy file
print("\n--- 7.9: Copy file ---")
try:
    shutil.copyfile('test.txt', 'test_copy.txt')
    print("Đã copy sang test_copy.txt")
except: pass

# Bài 7.10: Từ dài nhất
print("\n--- 7.10: Tìm từ dài nhất ---")
try:
    w = open('test.txt').read().split()
    if w:
        print(max(w, key=len))
except: pass
