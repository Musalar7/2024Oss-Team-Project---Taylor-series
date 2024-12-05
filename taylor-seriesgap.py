import sympy as sp
import numpy as np
import plotly.graph_objects as go

class TaylorSeriesPlotter:
    def __init__(self, function, variable='x'):
        self.function = sp.sympify(function)
        self.variable = sp.Symbol(variable)

    def taylor_series(self, center, order):
        return sp.series(self.function, self.variable, center, order + 1).removeO()

    def plot_comparison(self, center, orders, x_range=(-10, 10), num_points=500):
        x_vals = np.linspace(x_range[0], x_range[1], num_points)
        original_func = sp.lambdify(self.variable, self.function, modules="numpy")
        y_original = original_func(x_vals)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x_vals, y=y_original, mode='lines', name='Original Function'
        ))

        for order in orders:
            taylor_expr = self.taylor_series(center, order)
            taylor_func = sp.lambdify(self.variable, taylor_expr, modules="numpy")
            y_taylor = taylor_func(x_vals)

            fig.add_trace(go.Scatter(
                x=x_vals, y=y_taylor, mode='lines', name=f'Taylor Series (Order {order})'
            ))

        fig.update_layout(
            title=f"Taylor Series Approximation Comparison (Center: {center})",
            xaxis_title="x",
            yaxis_title="f(x)",
            legend_title="Functions",
            template="plotly_white"
        )

        fig.show()

if __name__ == "__main__":
    function_input = input("function (ex: sin(x), exp(x), log(1+x)): ")
    center_input = float(input("the center of the series: "))
    orders_input = input("degree (ex: 2,4,6): ")
    orders = list(map(int, orders_input.split(',')))

    plotter = TaylorSeriesPlotter(function_input)
    plotter.plot_comparison(center=center_input, orders=orders)