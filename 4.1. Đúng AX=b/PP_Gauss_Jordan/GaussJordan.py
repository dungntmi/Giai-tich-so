# GaussJordan giải HPT AX = B

import numpy as np
import pandas as pd

# GJ_Test1: test trường hợp phương trình có nghiệm
# GJ_Test2: test trường hợp phương trình vô số nghiệm
# GJ_Test3: test trường hợp phương trình vô nghiệm

df = pd.read_excel("GJ_Test3.xlsx", header=None)
matrix = df.to_numpy()
print("Ma trận mở rộng vừa nhập là:")
print(matrix)
print('===========================')

index_row = []
index_column = []
result = np.zeros((len(matrix[0]) - 1, len(matrix[0])))


# Gói tìm phần tử giải
def findPivot():
    global index_row, index_column
    index_temp = []
    pivot_element = 0
    for row in range(0, len(matrix)):
        if row in index_row:
            # Bỏ qua vì hàng này đã có phần tử giải
            continue
        # Tìm phần tử lớn nhất (giá trị tuyệt đối) trong hàng row
        max_row = np.amax(abs(matrix[row, 0:(len(matrix[0]) - 1)]))
        # Nếu có 1 hoặc -1 trong hàng row => chọn làm phần tử giải
        if (1 in matrix[row, 0:(len(matrix[0]) - 1)]) or (-1 in matrix[row, 0:(len(matrix[0]) - 1)]):
            pivot_element = 1
            row_pivot_element = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]) - 1)]) == pivot_element)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
            break
        # Lưu giá trị phần tử giải, tìm vị trí trên ma trận
        elif max_row > pivot_element:
            pivot_element = max_row
            row_pivot_element = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]) - 1)]) == pivot_element)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
    # Lưu vị trí hàng và cột của phần tử giải
    if pivot_element != 0:
        index_row.append(row_pivot_element)
        index_column.append(int(index_temp))
        print("Phần tử giải: ", round(matrix[index_row[-1]][index_column[-1]], 10))
        print("Vị trí: ", index_row[-1] + 1, index_column[-1] + 1)
        print()


# Gói GaussJordan khử ma trận
def GaussJordan():
    global matrix
    findPivot()
    # Tạo 1 ma trận không
    zeros_array = np.zeros((len(matrix), len(matrix[0])))
    for row in range(0, len(matrix)):
        if row == index_row[-1]:
            continue
        # Tìm m
        m = - matrix[row][index_column[-1]] / matrix[index_row[-1]][index_column[-1]]
        zeros_array[row] = matrix[index_row[-1]] * m
    matrix = matrix + zeros_array
    print(matrix)

# Gói chuẩn hóa hệ số
def normalizePivot():
    for i in range(len(index_row)):
        matrix[index_row[i]] = matrix[index_row[i]] / matrix[index_row[i]][index_column[i]]
    print('===========================')
    print("Chuẩn hóa hệ số:")
    print(matrix)
    print('===========================')


# Gói kiểm tra rank
def rank():
    # Hạng của ma trận hệ số A
    rank1 = 0
    # Hạng của ma trận mở rộng
    rank2 = 0
    for row in range(0, len(matrix)):
        if np.amax(abs(matrix[row, 0:(len(matrix[0]) - 1)])) > 0:
            rank1 = rank1 + 1
        if np.amax(abs(matrix[row, 0:len(matrix[0])])) > 0:
            rank2 = rank2 + 1
    if rank1 < rank2:
        print("Hệ phương trình vô nghiệm")
    elif rank1 < (len(matrix[0]) - 1):
        print("Hệ phương trình có vô số nghiệm")
        displaySolutions()
    else:
        print("Hệ phương trình có nghiệm duy nhất")
        displaySolutions()


# Hiển thị kết quả
def displaySolutions():
    global result
    for column in range(len(matrix[0]) - 1):
        if column in index_column:
            vt = index_column.index(column)
            result[column][0] = matrix[index_row[vt]][len(matrix[0]) - 1]
            for i in range(len(matrix[0]) - 1):
                if i not in index_column:
                    result[column][i + 1] = -matrix[index_row[vt]][i]
        else:
            result[column][column + 1] = 1

    # # In ma trận result ra màn hình
    # print('Ma tran ket qua:')
    # print(result)
    print('===========================')
    # In nghiệm (làm tròn đến 2 chữ số)
    print('Nghiệm của hệ phương trình:')
    for i in range(0, len(result)):
        print('X%d = ' % (i + 1), end='\t')
        for k in range(0, len(result[0])):
            if k == 0:
                print('%0.2f ' % (result[i, k]), end='+ ')
            else:
                print('%0.2f.X%d ' % (result[i, k], k), end='')
                if k == (len(result[0]) - 1):
                    print()
                else:
                    print('+ ', end='')

            # Kiểm tra xem liệu ma trận chỉ chứa số 0 hay không


isZero = np.all((matrix == 0))
if isZero:
    print('Lỗi vì ma trận chỉ chứa 0')
else:
    for i in range(0, min(len(matrix), len(matrix[0]))):
        GaussJordan()

    normalizePivot()
    rank()
    print('===========================')
