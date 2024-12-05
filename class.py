import sympy as sp
import numpy as np
import plotly.graph_objects as go

class TaylorSeriesPlotter:
    def __init__(self, function, variable='x'):
        self.function = sp.sympify(function)
        self.variable = sp.Symbol(variable)

    def taylor_series(self, center, order):
        return sp.series(self.function, self.variable, center, order + 1).removeO()

    def plot(self, center, order, x_range=(-10, 10), num_points=500):
        x_vals = np.linspace(x_range[0], x_range[1], num_points)
        original_func = sp.lambdify(self.variable, self.function, modules="numpy")
        taylor_expr = self.taylor_series(center, order)
        taylor_func = sp.lambdify(self.variable, taylor_expr, modules="numpy")
        y_original = original_func(x_vals)
        y_taylor = taylor_func(x_vals)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=y_original, mode='lines', name='Original Function'))
        fig.add_trace(go.Scatter(x=x_vals, y=y_taylor, mode='lines', name=f'Taylor Series (Order {order})'))
        fig.update_layout(
            title=f"Taylor Series Approximation (Center: {center}, Order: {order})",
            xaxis_title="x",
            yaxis_title="f(x)",
            legend_title="Functions",
            template="plotly_white"
        )
        fig.show()
