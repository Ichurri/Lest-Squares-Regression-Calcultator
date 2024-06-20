import matplotlib.pyplot as plt


def plot_points(n, points):
    # Desempaquetar los puntos en dos listas: xs y ys
    xs, ys = zip(*points)

    # Crear la gráfica
    plt.scatter(xs, ys)

    # Añadir etiquetas y título
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
    # Calcular la serie de datos d
    d = [y - (A + (B * x)) for x, y in zip(xs, ys)]
    return d


def calculate_d_squared(d):
    # Calcular la serie de datos d^2
    d_squared = [di ** 2 for di in d]
    return d_squared


def calculate_sigma_squared(d_squared, n):
    # Calcular sigma^2
    sigma_squared = sum(d_squared) / (n - 2)
    return sigma_squared


def calculate_delta(xs, n):
    # Calcular delta
    sum_x = sum(xs)
    sum_x2 = sum(x ** 2 for x in xs)
    delta = (n * sum_x2) - (sum_x ** 2)
    return delta


if __name__ == "__main__":
    # Solicitar al usuario la cantidad de pares de datos
    n = int(input("Introduce el número de pares de datos: "))

    # Solicitar los pares de datos
    points = []
    for i in range(n):
        x = float(input(f"Introduce x{i + 1}: "))
        y = float(input(f"Introduce y{i + 1}: "))
        points.append((x, y))

    # Graficar los puntos
    plot_points(n, points)

    # Calcular A y B
    xs, ys = zip(*points)
    A = calculate_A(xs, ys, n)
    B = calculate_B(xs, ys, n)
    print(f"El valor de A es: {A}")
    print(f"El valor de B es: {B}")

    # Calcular la serie de datos d
    d = calculate_d(xs, ys, A, B)

    # Calcular la serie de datos d^2
    d_squared = calculate_d_squared(d)

    # Calcular S
    S = sum(d_squared)
    print(f"El valor de S es: {S}")

    # Calcular sigma^2
    sigma_squared = calculate_sigma_squared(d_squared, n)
    print(f"El valor de σ^2 es: {sigma_squared}")

    # Calcular delta
    delta = calculate_delta(xs, n)
    print(f"El valor de Δ es: {delta}")
