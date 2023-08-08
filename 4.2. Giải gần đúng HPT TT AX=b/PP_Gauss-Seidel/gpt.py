'''
X=aX+b, nhưng b xấp xỉ thôi, không đúng chính xác đâu
sai số của code này là max[giá trị sau - trước] => epsilon tự tính
'''

import numpy as np

def gauss_seidel(A, B, x0, epsilon, max_iterations):
    n = A.shape[0]
    x = x0.copy()
    iteration = 0
    error = epsilon + 1

    while error > epsilon and iteration < max_iterations:
        x_prev = x.copy()

        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_prev[i+1:])
            x[i] = (B[i] - sigma) / A[i, i]

        error = np.linalg.norm(x - x_prev, np.inf)
        iteration += 1

        print("Iteration", iteration)
        print("Nghiệm:", x)
        print("Sai số:", error)
        print("-----------------------------")

    return x, error

# Đường dẫn tới file chứa ma trận mở rộng
file_path = "mt.txt"

# Đọc ma trận mở rộng từ file
matrix_data = np.loadtxt(file_path)
A = matrix_data[:, :-1]  # Ma trận hệ số
B = matrix_data[:, -1]  # Vectơ hằng số

# Kích thước của hệ phương trình
n = A.shape[0]

# Vectơ ban đầu
x0 = np.zeros(n)

# Sai số tuyệt đối cho phép
epsilon = 1e-6

# Số lần lặp tối đa
max_iterations = 1000

# Thực hiện phương pháp Gauss-Seidel
x, error = gauss_seidel(A, B, x0, epsilon, max_iterations)

# In ra kết quả cuối cùng
print("Kết quả:")
print("Nghiệm:", x)
print("Sai số:", error)
