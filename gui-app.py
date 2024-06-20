import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.figure import Figure
import math
import numpy as np

def plot_points(points, frame, title='Gráfica de puntos'):
    xs, ys = zip(*points)

    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.scatter(xs, ys)
    plot.set_xlabel('X')
    plot.set_ylabel('Y')
    plot.set_title(title)

    canvas = tkagg.FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def plot_calculated(xs, ys, A, B, frame, is_exponential):
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)

    # Plot original points
    plot.scatter(xs, ys, color='blue', label='Original Data')

    # Plot regression line
    regression_ys = [A + B * x for x in xs]
    if is_exponential:
        regression_ys = [math.exp(y) for y in regression_ys]
    plot.plot(xs, regression_ys, color='red', label='Regression Line')

    plot.set_xlabel('X')
    plot.set_ylabel('Y')
    plot.set_title('Regresión Lineal')
    plot.legend()

    canvas = tkagg.FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

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
    EA = math.sqrt((sum_x2 * sigma_squared) / delta)
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

def calculate_and_display_results():
    try:
        n = int(entry_n.get())
        points = []

        for i in range(n):
            x = float(entries_x[i].get())
            y = float(entries_y[i].get())
            points.append((x, y))

        equation_type = var_equation_type.get()
        is_exponential = (equation_type == "Exponencial")

        if is_exponential:
            points = [(math.log(x), math.log(y)) for x, y in points]

        # Limpiar las gráficas antes de dibujar nuevas
        for widget in frame_plot.winfo_children():
            widget.destroy()
        for widget in frame_calculated_plot.winfo_children():
            widget.destroy()

        plot_points(points, frame_plot, title='Datos Transformados' if is_exponential else 'Gráfica de puntos')

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

        label_A.config(text=f"El valor de A es: {A:.4f}")
        label_EA.config(text=f"El valor de EA es: {EA:.4f}")
        label_EA_percent.config(text=f"El valor de EA% es: {EA_percent:.4f}%")
        label_B.config(text=f"El valor de B es: {B:.4f}")
        label_EB.config(text=f"El valor de EB es: {EB:.4f}")
        label_EB_percent.config(text=f"El valor de EB% es: {EB_percent:.4f}%")
        label_sigma_squared.config(text=f"El valor de σ² es: {sigma_squared:.4f}")
        label_r_squared.config(text=f"El valor de r² es: {r**2:.4f}")
        label_delta.config(text=f"El valor de Δ es: {delta:.4f}")
        label_S.config(text=f"El valor de S es: {S:.4f}")

        plot_calculated(xs, ys, A, B, frame_calculated_plot, is_exponential)

    except ValueError as e:
        messagebox.showerror("Error", f"Error en la entrada de datos: {e}")

def create_entries():
    global entries_x, entries_y
    entries_x = []
    entries_y = []
    for i in range(int(entry_n.get())):
        entry_x = tk.Entry(window)
        entry_x.grid(row=i+4, column=0)
        entries_x.append(entry_x)

        entry_y = tk.Entry(window)
        entry_y.grid(row=i+4, column=1)
        entries_y.append(entry_y)

# Configuración de la ventana principal
window = tk.Tk()
window.title("Cálculo de Regresión Lineal o Exponencial")

# Crear widgets
label_n = tk.Label(window, text="Introduce el número de pares de datos:")
label_n.grid(row=0, column=0, columnspan=2)

entry_n = tk.Entry(window)
entry_n.grid(row=1, column=0, columnspan=2)

label_equation_type = tk.Label(window, text="Selecciona el tipo de ecuación:")
label_equation_type.grid(row=2, column=0, columnspan=2)

var_equation_type = tk.StringVar(value="Lineal")
radio_linear = tk.Radiobutton(window, text="Lineal", variable=var_equation_type, value="Lineal")
radio_linear.grid(row=3, column=0)
radio_exponential = tk.Radiobutton(window, text="Exponencial", variable=var_equation_type, value="Exponencial")
radio_exponential.grid(row=3, column=1)

button_create_entries = tk.Button(window, text="Crear entradas", command=create_entries)
button_create_entries.grid(row=3, column=2, columnspan=2)

button_calculate = tk.Button(window, text="Calcular y mostrar resultados", command=calculate_and_display_results)
button_calculate.grid(row=3, column=4, columnspan=2)

frame_plot = tk.Frame(window)
frame_plot.grid(row=4, column=2, columnspan=2, rowspan=10)

frame_calculated_plot = tk.Frame(window)
frame_calculated_plot.grid(row=4, column=4, columnspan=2, rowspan=10)

label_A = tk.Label(window, text="")
label_A.grid(row=14, column=0, columnspan=2)
label_EA = tk.Label(window, text="")
label_EA.grid(row=15, column=0, columnspan=2)
label_EA_percent = tk.Label(window, text="")
label_EA_percent.grid(row=16, column=0, columnspan=2)
label_B = tk.Label(window, text="")
label_B.grid(row=17, column=0, columnspan=2)
label_EB = tk.Label(window, text="")
label_EB.grid(row=18, column=0, columnspan=2)
label_EB_percent = tk.Label(window, text="")
label_EB_percent.grid(row=19, column=0, columnspan=2)
label_sigma_squared = tk.Label(window, text="")
label_sigma_squared.grid(row=20, column=0, columnspan=2)
label_r_squared = tk.Label(window, text="")
label_r_squared.grid(row=21, column=0, columnspan=2)
label_delta = tk.Label(window, text="")
label_delta.grid(row=22, column=0, columnspan=2)
label_S = tk.Label(window, text="")
label_S.grid(row=23, column=0, columnspan=2)

# Iniciar el loop principal
window.mainloop()
