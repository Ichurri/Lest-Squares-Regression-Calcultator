import matplotlib.pyplot as plt
import math


def plot_points(n, points):
    xs, ys = zip(*points)

    plt.scatter(xs, ys)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfica de puntos')

    # Mostrar la gráfica
    plt.show()


def calculate_A(xs, ys, n):
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_x2 = sum(x ** 2 for x in xs)
    sum_xy = sum(x * y for x, y in zip(xs, ys))

    numerator = (sum_y * sum_x2) - (sum_x * sum_xy)
    denominator = (sum_x2 * n) - (sum_x ** 2)

    A = numerator / denominator
    return A


def calculate_B(xs, ys, n):
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_x2 = sum(x ** 2 for x in xs)
    sum_xy = sum(x * y for x, y in zip(xs, ys))

    numerator = (sum_xy * n) - (sum_x * sum_y)
    denominator = (sum_x2 * n) - (sum_x ** 2)

    B = numerator / denominator
    return B


def calculate_d(xs, ys, A, B):
    d = [y - (A + (B * x)) for x, y in zip(xs, ys)]
    return d


def calculate_d_squared(d):
    d_squared = [di ** 2 for di in d]
    return d_squared


def calculate_sigma_squared(d_squared, n):
    sigma_squared = sum(d_squared) / (n - 2)
    return sigma_squared


def calculate_delta(xs, n):
    sum_x = sum(xs)
    sum_x2 = sum(x ** 2 for x in xs)
    delta = (n * sum_x2) - (sum_x ** 2)
    return delta


def calculate_EA(sum_x2, sigma_squared, delta):
    EA = math.sqrt((sum_x2 - sigma_squared) / delta)
    return EA


def calculate_EA_percent(EA, A):
    EA_percent = abs((EA / A) * 100)
    return EA_percent


def calculate_EB(sigma_squared, n, delta):
    EB = math.sqrt((sigma_squared * n) / delta)
    return EB


def calculate_EB_percent(EB, B):
    EB_percent = abs((EB / B) * 100)
    return EB_percent


def calculate_r(xs, ys, n):
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_x2 = sum(x ** 2 for x in xs)
    sum_y2 = sum(y ** 2 for y in ys)
    sum_xy = sum(x * y for x, y in zip(xs, ys))

    numerator = (sum_xy * n) - (sum_x * sum_y)
    denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

    result = numerator / denominator
    return result


if __name__ == "__main__":
    n = int(input("Introduce el número de pares de datos: "))

    points = []
    for i in range(n):
        x = float(input(f"Introduce x{i + 1}: "))
        y = float(input(f"Introduce y{i + 1}: "))
        points.append((x, y))

    plot_points(n, points)

    xs, ys = zip(*points)
    A = calculate_A(xs, ys, n)
    B = calculate_B(xs, ys, n)

    d = calculate_d(xs, ys, A, B)

    d_squared = calculate_d_squared(d)

    S = sum(d_squared)

    sigma_squared = calculate_sigma_squared(d_squared, n)

    delta = calculate_delta(xs, n)

    sum_x2 = sum(x ** 2 for x in xs)
    EA = calculate_EA(sum_x2, sigma_squared, delta)
    EA_percent = calculate_EA_percent(EA, A)

    EB = calculate_EB(sigma_squared, n, delta)
    EB_percent = calculate_EB_percent(EB, B)

    r = calculate_r(xs, ys, n)

    print(f"El valor de A es: {A}")
    print(f"El valor de EA es: {EA}")
    print(f"El valor de EA% es: {EA_percent}")
    print(f"El valor de B es: {B}")
    print(f"El valor de EB es: {EB}")
    print(f"El valor de EB% es: {EB_percent}")
    print(f"El valor de σ^2 es: {sigma_squared}")
    print(f"El valor de r^2 es: {r**2}")
    print(f"El valor de Δ es: {delta}")
    print(f"El valor de S es: {S}")
