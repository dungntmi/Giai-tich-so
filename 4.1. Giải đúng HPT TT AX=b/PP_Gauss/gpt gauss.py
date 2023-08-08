import numpy as np


def read_matrix_from_file(filename):
    """
    Đọc ma trận mở rộng từ file và trả về ma trận dưới dạng numpy array.
    Giả sử file chứa các số cách nhau bởi khoảng trắng,
    mỗi dòng tương ứng với một hàng của ma trận mở rộng.
    """
    matrix = []
    with open('matrix.txt', 'r') as file:
        for line in file:
            row = [float(x) for x in line.split()]
            matrix.append(row)
    return np.array(matrix)


def print_augmented_matrix(matrix):
    """
    In ma trận mở rộng.
    """
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


def gaussian_elimination(matrix):
    """
    Áp dụng phương pháp Gauss để giải hệ phương trình tuyến tính.
    """
    num_rows, num_cols = matrix.shape
    for i in range(num_rows):
        # Tìm phần tử không bằng 0 đầu tiên trong cột i
        nonzero_row = None
        for j in range(i, num_rows):
            if matrix[j, i] != 0:
                nonzero_row = j
                break

        if nonzero_row is None:
            continue  # Cột i toàn bộ là 0, bỏ qua

        # Đổi chỗ hàng i với hàng có phần tử không bằng 0 đầu tiên
        matrix[[i, nonzero_row]] = matrix[[nonzero_row, i]]

        # Khử các phần tử ở các hàng dưới hàng i
        for j in range(i + 1, num_rows):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j] -= factor * matrix[i]

        print("Bước khử số", i + 1)
        print_augmented_matrix(matrix)
        print()

    return matrix


# Đọc ma trận mở rộng từ file
filename = "matrix.txt"  # Thay đổi tên file thành tên file thực tế
augmented_matrix = read_matrix_from_file(filename)

# In ma trận mở rộng ban đầu
print("Ma trận mở rộng ban đầu:")
print_augmented_matrix(augmented_matrix)
print()

# Áp dụng phương pháp Gauss
result = gaussian_elimination(augmented_matrix)

# In kết quả
print("Kết quả:")
for i in range(result.shape[0]):
    print(f"x{i + 1} =", result[i, -1])
