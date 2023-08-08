import numpy as np

# Hàm tính sai số theo chuẩn vô cùng
def infinity_norm(x, y):
    return np.max(np.abs(x - y))

# Hàm giải hệ phương trình bằng phương pháp Jacobi
def jacobi_method(A, b, epsilon=0.01, max_iterations=30):
    n = len(A)
    x = np.zeros(n)  # Giả sử nghiệm ban đầu là vectơ 0
    x_prev = np.zeros(n)  # Nghiệm của lần lặp trước đó

    for iteration in range(max_iterations):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x_prev[:i]) - np.dot(A[i, i+1:], x_prev[i+1:])) / A[i, i]

        error = infinity_norm(x, x_prev)  # Tính sai số

        print(f"Bước lặp {iteration+1}: {x} (Sai số: {error})")

        if error < epsilon:  # Kiểm tra điều kiện dừng
            break

        x_prev = x.copy()  # Cập nhật nghiệm của lần lặp trước

    return x

# Đường dẫn tới file chứa ma trận mở rộng
file_path = "jacobi.txt"

# Đọc ma trận mở rộng từ file
matrix_data = np.loadtxt(file_path)
A = matrix_data[:, :-1]  # Ma trận hệ số
b = matrix_data[:, -1]  # Vectơ hằng số

# Giải hệ phương trình bằng phương pháp Jacobi
solution = jacobi_method(A, b)
print("Nghiệm:", solution)
