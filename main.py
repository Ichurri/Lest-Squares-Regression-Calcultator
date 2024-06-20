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
