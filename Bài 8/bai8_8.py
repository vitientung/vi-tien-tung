from tkinter import *

def submit_info():
    # Hàm này có thể được sử dụng để xử lý dữ liệu sau này
    print("Thông tin đã được gửi/xử lý!")

root = Tk()
root.title("Bài 8.8: Form Thông tin")
root.geometry("300x250") # Thiết lập kích thước cửa sổ

# --- Họ tên ---
Label(root, text="Họ tên:").pack(pady=2)
Entry(root).pack()

# --- MSSV ---
Label(root, text="MSSV:").pack(pady=2)
Entry(root).pack()

# --- Giới tính (Radio Buttons) ---
Label(root, text="Giới tính:").pack(pady=5)
v = IntVar()
Radiobutton(root, text="Nam", variable=v, value=1).pack()
Radiobutton(root, text="Nữ", variable=v, value=2).pack()

# --- Nút Gửi ---
Button(root, text="Gửi", command=submit_info, bg="blue", fg="white").pack(pady=10)

root.mainloop()
