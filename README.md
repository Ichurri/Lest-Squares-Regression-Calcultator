# Regression Analysis GUI Application

This application provides a graphical user interface (GUI) to perform linear or exponential regression analysis on a given set of data points. It calculates various statistical parameters and displays the results along with a plot of the data and the fitted regression line.

## Features

- **Input Data Pairs**: Users can input any number of (x, y) data pairs.
- **Select Equation Type**: Choose between linear and exponential regression.
- **Calculate Parameters**: Computes parameters like A, B, sigma squared, correlation coefficient (r²), and more.
- **Error Analysis**: Provides error estimations and their percentages for the calculated parameters.
- **Plot Results**: Displays a scatter plot of the original data along with the regression line.
- **Interactive GUI**: Easy-to-use interface built with Tkinter and Matplotlib.

## Requirements

- Python 3.x
- Tkinter
- Matplotlib

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

   ```bash
      pip install tkinter matplotlib
    ```
## Usage
1. Run the script:
   ```bash
      python gui-app.py
   ```
2. Enter the number of data pairs and the type of equation (linear or exponential).
3. Input the x and y values for each data pair.
4. Click "Create entries" to generate input fields for the data pairs.
5. Enter the real value of parameter b.
6. Click "Calculate and display results" to compute and display the results.

## Functions
### Calculate Functions
- calculate_A(xs, ys, n): Computes parameter A.
- calculate_B(xs, ys, n): Computes parameter B.
- calculate_d(xs, ys, A, B): Computes the differences between observed and predicted values.
- calculate_d_squared(d): Computes the squared differences.
- calculate_sigma_squared(d_squared, n): Computes the variance of residuals.
- calculate_delta(xs, n): Computes the delta value for further calculations.
- calculate_EA(sum_x2, sigma_squared, delta): Computes the standard error for A.
- calculate_EA_percent(EA, A): Computes the percentage error for A.
- calculate_a(A): Computes the exponential of A for exponential regression.
- calculate_Ea(a, EA): Computes the standard error for a in exponential regression.
- calculate_Ea_percent(Ea, a): Computes the percentage error for a.
- calculate_EB(sigma_squared, n, delta): Computes the standard error for B.
- calculate_EB_percent(EB, B): Computes the percentage error for B.
- calculate_r(xs, ys, n): Computes the correlation coefficient.
- calculate_D_percent(B, b_real): Computes the percentage difference between calculated and real B.

## GUI Functions
- create_entries(): Creates input fields for data pairs.
- calculate_and_display_results(): Validates inputs, performs calculations, and updates the GUI with results.
- plot_calculated(xs, ys, A, B, frame, is_exponential): Plots the original data and regression line.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for GUI components.
- [Matplotlib](https://matplotlib.org/) for plotting capabilities.

