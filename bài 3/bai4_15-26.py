# Bài 4.15 -> 4.26
print("\n--- 4.15: Sắp xếp từ ---")
inp = input("Nhập các từ: ").split()
print(" ".join(sorted(set(inp))))

print("\n--- 4.16: In số nhị phân ---")
inp = input("Nhập chuỗi nhị phân (phân tách phẩy): ").split(',')
print(",".join(inp))

print("\n--- 4.17: Tổng ước số > chính nó ---")
n = int(input("Nhập n: "))
def check_uoc(num):
    return sum(i for i in range(1, num) if num%i==0) > num
print([i for i in range(1, n) if check_uoc(i)])

print("\n--- 4.18: Fibonacci < n ---")
n = int(input("Nhập n: "))
fib = [0, 1]
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
print([x for x in fib if x < n])

print("\n--- 4.19: Tuple số nguyên tố < 1000 ---")
primes = [x for x in range(2, 1000) if all(x%i!=0 for i in range(2, int(x**0.5)+1))]
print(tuple(primes))

print("\n--- 4.20: Tam giác Pascal ---")
n = int(input("Số dòng: "))
r = [1]
for i in range(n):
    print(r)
    r = [sum(x) for x in zip([0]+r, r+[0])]

print("\n--- 4.21: Nhị phân chia hết cho 5 ---")
items = input("Nhập 4 số nhị phân (phẩy): ").split(',')
print(",".join([p for p in items if int(p, 2) % 5 == 0]))

print("\n--- 4.22: Số toàn chẵn (1000-3000) ---")
res = [str(i) for i in range(1000, 3001) if all(int(c)%2==0 for c in str(i))]
print(",".join(res))

print("\n--- 4.23: Đếm chữ/số ---")
s = input("Nhập câu: ")
print(f"Chữ: {sum(c.isalpha() for c in s)}, Số: {sum(c.isdigit() for c in s)}")

print("\n--- 4.24: Đếm Hoa/Thường ---")
s = input("Nhập câu: ")
print(f"Hoa: {sum(c.isupper() for c in s)}, Thường: {sum(c.islower() for c in s)}")

print("\n--- 4.25: Lọc số lẻ ---")
inp = input("Nhập dãy số (phẩy): ").split(',')
print(",".join([x for x in inp if int(x)%2!=0]))

print("\n--- 4.26: Ngân hàng ---")
total = 0
print("Nhập D 100 hoặc W 50 (Enter để dừng):")
while True:
    val = input()
    if not val: break
    op, num = val.split()
    total += int(num) if op=='D' else -int(num)
print(f"Tổng tiền: {total}")
