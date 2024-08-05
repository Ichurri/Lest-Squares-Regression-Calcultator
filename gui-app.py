import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.figure import Figure
import math

def plot_calculated(xs, ys, A, B, frame, is_exponential):
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)

    plot.scatter(xs, ys, color='blue', label='Original Data')

    plot.set_xlabel('X')
    plot.set_ylabel('Y')
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

def calculate_a(A):
    a = math.exp(A)
    return a

def calculate_Ea(a, EA):
    Ea = a * EA
    return Ea

def calculate_Ea_percent(Ea, a):
    Ea_percent = abs((Ea / a) * 100)
    return Ea_percent

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

def calculate_D_percent(B, b_real):
    D_percent = abs((B - b_real) / b_real) * 100
    return D_percent

def calculate_and_display_results():
    try:
        n = num_entries 
        points = []

        for i in range(n):
            x = float(entries_x[i].get())
            y = float(entries_y[i].get())
            points.append((x, y))

        equation_type = var_equation_type.get()
        is_exponential = (equation_type == "Exponential")

        xs, ys = zip(*points)
        if is_exponential:
            log_xs = [math.log(x) for x in xs]
            log_ys = [math.log(y) for y in ys]
            A = calculate_A(log_xs, log_ys, n)
            B = calculate_B(log_xs, log_ys, n)
            a = calculate_a(A)
        else:
            A = calculate_A(xs, ys, n)
            B = calculate_B(xs, ys, n)
            a = None

        d = calculate_d(log_xs if is_exponential else xs, log_ys if is_exponential else ys, A, B)
        d_squared = calculate_d_squared(d)
        S = sum(d_squared)
        sigma_squared = calculate_sigma_squared(d_squared, n)
        delta = calculate_delta(log_xs if is_exponential else xs, n)

        sum_x2 = sum(x ** 2 for x in (log_xs if is_exponential else xs))
        EA = calculate_EA(sum_x2, sigma_squared, delta)
        EA_percent = calculate_EA_percent(EA, A)
        Ea = calculate_Ea(a, EA) if is_exponential else None
        Ea_percent = calculate_Ea_percent(Ea, a) if is_exponential else None
        EB = calculate_EB(sigma_squared, n, delta)
        EB_percent = calculate_EB_percent(EB, B)
        r = calculate_r(log_xs if is_exponential else xs, log_ys if is_exponential else ys, n)

        b_real = float(entry_b_real.get())
        D_percent = calculate_D_percent(B, b_real)

        label_A.config(text=f"The value of A is: {A:.4f}")
        label_EA.config(text=f"The value of EA is: {EA:.4f}")
        label_EA_percent.config(text=f"The value of EA% is: {EA_percent:.4f}%")
        label_B.config(text=f"The value of B is: {B:.4f}")
        label_EB.config(text=f"The value of EB is: {EB:.4f}")
        label_EB_percent.config(text=f"The value of EB% is: {EB_percent:.4f}%")
        label_sigma_squared.config(text=f"The value of σ² is: {sigma_squared:.4f}")
        label_r_squared.config(text=f"The value of r² is: {r ** 2:.4f}")
        label_delta.config(text=f"The value of Δ is: {delta:.4f}")
        label_S.config(text=f"The value of S is: {S:.4f}")
        label_D_percent.config(text=f"The value of D% is: {D_percent:.4f}%")

        if is_exponential:
            label_a.config(text=f"The value of A is: {a:.4f}")
            label_Ea.config(text=f"The value of EA is: {Ea:.4f}")
            label_Ea_percent.config(text=f"The value of EA% is: {Ea_percent:.4f}%")
        else:
            label_a.config(text="")
            label_Ea.config(text="")
            label_Ea_percent.config(text="")

        plot_calculated(xs, ys, A, B, frame_plot, is_exponential)

    except ValueError as e:
        messagebox.showerror("Error", f"Error in the data entry: {e}")

def create_entries():
    global entries_x, entries_y, num_entries
    entries_x = []
    entries_y = []

    # Obtener el valor de entry_n antes de destruirlo
    num_entries = int(entry_n.get())

    # Destruir los widgets antiguos
    label_n.destroy()
    entry_n.destroy()
    label_equation_type.destroy()
    radio_linear.destroy()
    radio_exponential.destroy()

    label_x_column = tk.Label(frame_inputs, text="x")
    label_x_column.grid(row=0, column=0, padx=5, pady=2)
    label_y_column = tk.Label(frame_inputs, text="y")
    label_y_column.grid(row=0, column=1, padx=5, pady=2)

    for i in range(num_entries):
        entry_x = tk.Entry(frame_inputs)
        entry_x.grid(row=i + 1, column=0, padx=5, pady=2)
        entries_x.append(entry_x)

        entry_y = tk.Entry(frame_inputs)
        entry_y.grid(row=i + 1, column=1, padx=5, pady=2)
        entries_y.append(entry_y)

window = tk.Tk()
window.title("Calculation of Linear or Exponential Regression")

style = ttk.Style()
style.theme_use('clam')

frame_inputs = tk.Frame(window)
frame_inputs.grid(row=0, column=0, padx=5, pady=5)

label_n = tk.Label(frame_inputs, text="Enter the number of data pairs:")
label_n.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

entry_n = tk.Entry(frame_inputs)
entry_n.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

label_equation_type = tk.Label(frame_inputs, text="Select the type of equation:")
label_equation_type.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

var_equation_type = tk.StringVar(value="Lineal")
radio_linear = ttk.Radiobutton(frame_inputs, text="Lineal", variable=var_equation_type, value="Lineal")
radio_linear.grid(row=3, column=0, padx=5, pady=5)
radio_exponential = ttk.Radiobutton(frame_inputs, text="Exponencial", variable=var_equation_type, value="Exponential")
radio_exponential.grid(row=3, column=1, padx=5, pady=5)

label_b_real = tk.Label(frame_inputs, text="Enter the real value of b:")
label_b_real.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

entry_b_real = tk.Entry(frame_inputs)
entry_b_real.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

button_create_entries = ttk.Button(frame_inputs, text="Create entries", command=create_entries)
button_create_entries.grid(row=3, column=4, columnspan=2, padx=5, pady=5)

button_calculate = ttk.Button(frame_inputs, text="Calculate and display results", command=calculate_and_display_results)
button_calculate.grid(row=3, column=6, columnspan=2, padx=5, pady=5)

frame_results = tk.Frame(window)
frame_results.grid(row=0, column=1, padx=5, pady=5)

label_A = tk.Label(frame_results, text="")
label_A.grid(row=0, column=0, padx=5, pady=2)
label_EA = tk.Label(frame_results, text="")
label_EA.grid(row=1, column=0, padx=5, pady=2)
label_EA_percent = tk.Label(frame_results, text="")
label_EA_percent.grid(row=2, column=0, padx=5, pady=2)
label_B = tk.Label(frame_results, text="")
label_B.grid(row=3, column=0, padx=5, pady=2)
label_EB = tk.Label(frame_results, text="")
label_EB.grid(row=4, column=0, padx=5, pady=2)
label_EB_percent = tk.Label(frame_results, text="")
label_EB_percent.grid(row=5, column=0, padx=5, pady=2)
label_sigma_squared = tk.Label(frame_results, text="")
label_sigma_squared.grid(row=6, column=0, padx=5, pady=2)
label_r_squared = tk.Label(frame_results, text="")
label_r_squared.grid(row=7, column=0, padx=5, pady=2)
label_delta = tk.Label(frame_results, text="")
label_delta.grid(row=8, column=0, padx=5, pady=2)
label_S = tk.Label(frame_results, text="")
label_S.grid(row=9, column=0, padx=5, pady=2)
label_D_percent = tk.Label(frame_results, text="")
label_D_percent.grid(row=10, column=0, padx=5, pady=2)
label_a = tk.Label(frame_results, text="")
label_a.grid(row=11, column=0, padx=5, pady=2)
label_Ea = tk.Label(frame_results, text="")
label_Ea.grid(row=12, column=0, padx=5, pady=2)
label_Ea_percent = tk.Label(frame_results, text="")
label_Ea_percent.grid(row=13, column=0, padx=5, pady=2)

frame_plot = tk.Frame(window)
frame_plot.grid(row=0, column=2, padx=5, pady=5)

window.mainloop()
