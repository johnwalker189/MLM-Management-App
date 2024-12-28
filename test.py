import tkinter as tk

def format_currency(event):
    # Lấy giá trị hiện tại từ ô Entry
    value = entry.get()
    
    # Xóa các dấu phẩy cũ (nếu có) và kiểm tra tính hợp lệ
    value = value.replace(",", "")
    if value.isdigit():
        # Thêm dấu phẩy vào số tiền
        formatted_value = "{:,}".format(int(value))
        # Cập nhật lại nội dung ô Entry
        entry.delete(0, tk.END)
        entry.insert(0, formatted_value)
    elif value == "":
        # Nếu người dùng xóa hết, giữ ô Entry trống
        entry.delete(0, tk.END)
    else:
        # Nếu không hợp lệ, hiển thị thông báo
        tk.messagebox.showwarning("Invalid Input", "Please enter only numbers!")
        entry.delete(0, tk.END)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Currency Formatter")

# Tạo ô Entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=20)

# Ràng buộc sự kiện `<KeyRelease>` với hàm định dạng
entry.bind("<KeyRelease>", format_currency)

# Chạy ứng dụng
root.mainloop()
