import numpy as np


def svd_decomposition(matrix):
    U, s, VT = np.linalg.svd(matrix, full_matrices=True)
    return U, s, VT


def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = [[float(num) for num in line.split()] for line in lines]
        return np.array(matrix)


# Đường dẫn tới file chứa ma trận A
file_path = "input.txt"

# Đọc ma trận A từ file
A = read_matrix_from_file(file_path)

# Thực hiện phân tích SVD
U, s, VT = svd_decomposition(A)

print("Ma trận A:")
print(A)
print("\nMa trận U:")
print(U)
print("\nGiá trị suy biến:")
print(s)
print("\nMa trận chuyển vị VT:")
print(VT)
