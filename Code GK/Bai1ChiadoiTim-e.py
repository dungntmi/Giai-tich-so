import math

def compute_e(epsilon):
    # Tìm xấp xỉ của số e với sai số epsilon từ phương trình lnx-1=0
    a = 1.0  # Giới hạn dưới
    b = 3.0  # Giới hạn trên

    iterations = 0  # Đếm số lần lặp
    while (b - a) > epsilon:
        c = (a + b) / 2.0
        if math.log(c) - 1.0 > 0:
            b = c
        else:
            a = c

        iterations += 1
        if iterations <= 3 or (b - a) <= epsilon:
            print("Lần lặp {}: e ~ {}".format(iterations, (a + b) / 2.0))

    e = (a + b) / 2.0
    return e


# Chạy thử thuật toán
epsilon = 1e-6  # Sai số epsilon cho trước

e_value = compute_e(epsilon)

print("Giá trị của e là:", e_value)
