import numpy as np

# Bài 5.4: Đảo ngược mảng NumPy
print("--- 5.4: Đảo ngược mảng NumPy ---")
x = np.arange(12, 38)
print(x[::-1])

# Bài 5.5 & 5.6: Min/Max và vị trí
print("\n--- 5.5 & 5.6: Min/Max List ---")
lst_demo = [10, 50, 2, 8, 99, 4]
mn, mx = min(lst_demo), max(lst_demo)
print(f"Min: {mn} (vị trí {lst_demo.index(mn)})")
print(f"Max: {mx} (vị trí {lst_demo.index(mx)})")

# Bài 5.11: Sắp xếp theo Lớp, Chiều cao (Đã sửa kiểu chuỗi)
print("\n--- 5.11: Sắp xếp theo Lớp & Chiều cao ---")
# Dùng 'U10' cho Unicode string
dt = [('name', 'U10'), ('class', int), ('height', float)] 
vals = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.1), ('Pit', 5, 40.11)]
arr = np.array(vals, dtype=dt)
print(np.sort(arr, order=['class', 'height']))

# Bài 5.12: Lexsort (Id và Chiều cao)
print("\n--- 5.12: Lexsort ---")
ids = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
hgs = np.array([40., 42., 45., 41., 38., 40., 42.0])
ind = np.lexsort((ids, hgs))
print("Dữ liệu sau sắp xếp:")
for i in ind:
    print(f"ID: {ids[i]}, Height: {hgs[i]}")
