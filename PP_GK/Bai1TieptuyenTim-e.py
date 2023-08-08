import math

def compute_e(epsilon):
    # Tính xấp xỉ của số e với sai số epsilon từ phương trình lnx-1=0 bằng phương pháp tiếp tuyến (Newton-Raphson)
    x = 2.0  # Giá trị khởi tạo

    iterations = 0  # Đếm số lần lặp
    while True:
        fx = math.log(x) - 1.0  # Giá trị hàm số tại x
        f_prime_x = 1 / x  # Giá trị đạo hàm tại x
        delta_x = -fx / f_prime_x  # Số delta x để tiếp tục tiếp tuyến

        x += delta_x  # Cập nhật x

        iterations += 1
        if iterations <= 3 or abs(delta_x) <= epsilon:
            print("Lần lặp {}: e ~ {}".format(iterations, x))

        if abs(delta_x) <= epsilon:
            break

    return x, iterations


# Chạy thử thuật toán
epsilon = 1e-15  # Sai số epsilon cho trước

e_value, num_iterations = compute_e(epsilon)

print("Giá trị của e là:", e_value)
print("Số lần lặp:", num_iterations)
