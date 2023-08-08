# SVD

import numpy as np
from numpy import linalg as la
from scipy.linalg import *

# Input: Ma trận A cỡ m x n
# Test1: TH m = 2 < n = 3
# Test2: TH m = 3 = n = 3
# Test3: TH m = 3 > n = 2
# Test4: TH m = 2 < n = 3 với r = 1 khác m
# Test5: TH m = 3 > n = 2 với r = 1 khác n
A = np.loadtxt('input.txt', delimiter=' ')

# m hàng, n cột
(m, n) = np.shape(A)
print('Số hàng:', m)
print('Số cột:', n)


# Hàm tìm 3 ma trận U, S, V thỏa mãn A = U.S.V^{T}
def SVD(A):
    np.seterr(invalid='ignore')
    # Gán ma trận Sigma bằng ma trận 0 cỡ m x n
    sigma = np.zeros((m, n))
    v = np.eye(n)

    # r = Rank(A)
    r = np.linalg.matrix_rank(A)
    print('rank(A) =', r)

    # TH1: m >= n
    if m >= n:
        # Tìm ma trận U
        # Tìm các giá trị riêng w_{i} của A.A^{T}
        # Tìm các vector riêng tương ứng là u_{i}
        w, u = la.eig(A @ A.T)
        print('\nCác trị riêng của A.A^{T}:')
        print(w)
        print('\nCác vector riêng tương ứng:')  # Vertically
        print(u)

        # Sắp xếp các giá trị riêng và các vetor riêng tương ứng theo giá trị riêng giảm dần từ trái qua phải
        for i in range(m - 1):
            for j in range(i + 1, m):
                if (w[j - 1] < w[j]):
                    w[j], w[j - 1] = w[j - 1], w[j]
                    u[:, [j - 1, j]] = u[:, [j, j - 1]]
        U = u

        # Tìm ma trận V
        # Trong TH ma trận A không đủ hạng
        # Ta tìm r vector riêng đầu tiên ứng với V

        # Từ U tính ra V
        V = np.zeros((r, n))
        for i in range(r):
            V[i, :n] = (u.T[i, :m] @ A) / (np.sqrt(w[i]))

        # Tìm (n - r) vector còn lại
        # Ta tìm ker(A)
        if r != n:
            ns = null_space(A)
            ns = ns.T
            V = np.concatenate((V, ns), axis=0)

        # V = V^{T}
        V = V.T

        # Tìm ma trận Sigma
        np.fill_diagonal(sigma, np.sqrt(w))

    # TH2: m < n
    # Tương tự như TH1, chỉ đổi vai trò của U và V
    else:
        # Tìm ma trận V
        w, v = la.eig(A.T @ A)
        print('\nCác trị riêng của A^{T}.A:')
        print(w)
        print('\nCác vector riêng tương ứng:')  # Vertically
        print(v)

        # Sắp xếp các giá trị riêng và các vetor riêng tương ứng theo giá trị riêng giảm dần từ trái qua phải
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (w[j - 1] < w[j]):
                    w[j], w[j - 1] = w[j - 1], w[j]
                    v[:, [j - 1, j]] = v[:, [j, j - 1]]

        V = v

        # Tìm ma trận U
        # Trong TH ma trận A không đủ hạng
        # Ta tìm r vector riêng đầu tiên ứng với V

        # Từ V tính ra U
        U = np.zeros((r, m))
        for i in range(r):
            U[i, :m] = (v.T[i, :n] @ A.T) / (np.sqrt(w[i]))

        # Tìm (m - r) vector còn lại
        # Ta tìm ker(A^{T})
        if r != m:
            nd = null_space(A.T)
            nd = nd.T
            U = np.concatenate((U, nd), axis=0)

        # U = U^{T}
        U = U.T

        # Tìm ma trận Sigma
        np.fill_diagonal(sigma, np.sqrt(w))

    return U, sigma, V


U, sigma, V = SVD(A)
print("\nA = ")
print(A)
print("\nU = ")
print(U)
print("\nS = ")
print(sigma)
print("\nV = ")
print(V)
print("\nKiểm tra:")
print('A - U.S.V^{T} = 0')
print(A - U @ sigma @ V.T)
print("\nKiểm tra ma trận trực giao:")
print('U^{-1} - U^{T} = 0')
print(la.inv(U) - U.T)
print('\nV^{-1} - V^{T} = 0')
print(la.inv(V) - V.T)

print("\nSo sánh với hàm svd()")
U_SVD, S_SVD, V_SVD = svd(A)
print("U = ")
print(U_SVD)
print("\nS = ")
print(S_SVD)
print("\nV^{T} = ")
print(V_SVD)