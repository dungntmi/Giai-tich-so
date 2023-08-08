import numpy as np


def power_iteration(A, epsilon=1e-6, max_iterations=1000):
    n = A.shape[0]
    x = np.random.rand(n)  # Chọn vector ngẫu nhiên là vector bắt đầu
    x /= np.linalg.norm(x, 2)  # Chuẩn hóa vector

    for _ in range(max_iterations):
        y = A @ x  # Tính vector mới
        eigenvalue = np.dot(x, y)  # Tính giá trị riêng dự kiến

        x_new = y / np.linalg.norm(y, 2)  # Chuẩn hóa vector mới

        # Tính sai số giữa hai vector
        delta = np.linalg.norm(x_new - x, 2)

        if delta < epsilon:
            break

        x = x_new

    eigenvector = x_new
    eigenvalue = eigenvalue

    return eigenvalue, eigenvector


# Ví dụ sử dụng
A = np.array([[4, -1, 1],
              [-1, 3, -2],
              [1, -2, 3]])

eigenvalue, eigenvector = power_iteration(A)

print("Giá trị kỳ dị lớn nhất:", eigenvalue)
print("Vector kỳ dị phải/trái:", eigenvector)
