import math

# Bài 6.2: Class Hình Chữ Nhật
class HCN:
    def __init__(self, d, r):
        self.d = d
        self.r = r
    def area(self): return self.d * self.r

print("--- 6.2: Diện tích HCN (10, 5) ---")
print(HCN(10, 5).area())

# Bài 6.7: Class Circle (Đã sửa dùng math.pi)
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r**2
    def perim(self): return 2 * math.pi * self.r

print("\n--- 6.7: Hình tròn (r=5) ---")
c = Circle(5)
print(f"Diện tích: {c.area():.2f}, Chu vi: {c.perim():.2f}")
