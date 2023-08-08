import numpy as np


def svd_approximation(matrix, k):
    # Tính SVD cắt ngắn với số thành phần k
    U, s, VT = np.linalg.svd(matrix, full_matrices=False)

    # Lấy k thành phần hàng đầu của ma trận U, k giá trị suy biến hàng đầu, và k cột đầu tiên của ma trận V^T
    U_k = U[:, :k]
    s_k = np.diag(s[:k])
    VT_k = VT[:k, :]

    # Tính giá trị kỳ dị lớn nhất
    sigma_max = s[0]

    # Tính vector kỳ dị trái và phải tương ứng
    u_kydi_left = U_k[:, 0]
    v_kydi_right = VT_k[0, :]

    return sigma_max, u_kydi_left, v_kydi_right


# Ví dụ về phân tích SVD cắt ngắn cho ma trận A
def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = [[float(num) for num in line.split()] for line in lines]
        return np.array(matrix)


# Đường dẫn tới file chứa ma trận A
file_path = "input.txt"

# Đọc ma trận A từ file
A = read_matrix_from_file(file_path)

# Số thành phần cần xấp xỉ (k)
k = 1

# Thực hiện phân tích SVD cắt ngắn
sigma_max, u_kydi_left, v_kydi_right = svd_approximation(A, k)

print("Giá trị kỳ dị lớn nhất (σ_max):", sigma_max)
print("Vector kỳ dị trái (u_kydi_left):", u_kydi_left)
print("Vector kỳ dị phải (v_kydi_right):", v_kydi_right)
