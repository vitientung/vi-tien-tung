import math

# --- BÀI 1: THUẬT TOÁN FLOWGORITHM ---
print("\n" + "="*20 + " BÀI 1 " + "="*20)

# Bài 1.d: Diện tích tam giác
print("--- 1.d: Tính diện tích tam giác ---")
canh = float(input("Nhập cạnh đáy: "))
cao = float(input("Nhập chiều cao: "))
print(f"Kết quả: Diện tích = {0.5 * canh * cao}")

# Bài 1.e: Kiểm tra số nguyên tố
print("\n--- 1.e: Kiểm tra số nguyên tố ---")
n = int(input("Nhập số nguyên dương n: "))
if n < 2:
    print(f"{n} không phải là số nguyên tố")
else:
    la_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break
    print(f"{n} {'là' if la_nguyen_to else 'không phải là'} số nguyên tố")


# --- BÀI 2: CẤU TRÚC ĐIỀU KHIỂN ---
print("\n" + "="*20 + " BÀI 2 " + "="*20)

# Bài 2.13: Giải phương trình bậc 2
print("--- 2.13: Giải phương trình ax^2 + bx + c = 0 ---")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        print("Vô nghiệm" if c != 0 else "Vô số nghiệm")
    else:
        print(f"Phương trình bậc 1, x = {-c/b}")
else:
    delta = b*b - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"2 nghiệm phân biệt: x1={x1:.2f}, x2={x2:.2f}")
    elif delta == 0:
        print(f"Nghiệm kép: x = {-b/(2*a):.2f}")
    else:
        print("Vô nghiệm")


# --- BÀI 3: LẬP TRÌNH HÀM ---
print("\n" + "="*20 + " BÀI 3 " + "="*20)

# Bài 3.10: Hàm hình tròn
def tinh_hinh_tron(r):
    if r <= 0: return "Bán kính sai"
    cv = 2 * math.pi * r
    dt = math.pi * r**2
    return f"Chu vi: {cv:.2f}, Diện tích: {dt:.2f}"

print("--- 3.10: Tính hình tròn ---")
r_input = float(input("Nhập bán kính: "))
print(tinh_hinh_tron(r_input))

# Bài 3.11: Hàm lãi suất
def tinh_lai_suat(t, n, k):
    return n * ((1 + t/100)**k)

print("\n--- 3.11: Tính lãi suất ---")
lai = float(input("Lãi suất (%/tháng): "))
von = float(input("Vốn gốc: "))
thang = int(input("Số tháng: "))
print(f"Tổng tiền nhận được: {tinh_lai_suat(lai, von, thang):.2f}")
