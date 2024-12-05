import sympy as sp
import numpy as np
import plotly.graph_objects as go

def taylor_series_comparison():
    formula_input = input("함수 입력 (예: sin(x), exp(x), x**2): ")
    x = sp.Symbol('x')
    formula = sp.sympify(formula_input)

    degrees = input("비교할 테일러 급수 차수 입력 (쉼표로 구분, 예: 2, 4, 6): ")
    degrees = [int(degree.strip()) for degree in degrees.split(',')]

    taylor_series_list = [
        (degree, sp.series(formula, x, 0, degree + 1).removeO()) for degree in degrees
    ]

    print("테일러 급수:")
    for degree, taylor in taylor_series_list:
        print(f"{degree}차: {taylor}")

    plot_taylor_series_comparison(formula, taylor_series_list)

def plot_taylor_series_comparison(formula, taylor_series_list):
    x_vals = np.linspace(-10, 10, 500)
    x = sp.Symbol('x')

    original_func = sp.lambdify(x, formula, "numpy")
    y_original = original_func(x_vals)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_original, mode='lines', name='원래 함수'))

    for degree, taylor in taylor_series_list:
        taylor_func = sp.lambdify(x, taylor, "numpy")
        y_taylor = taylor_func(x_vals)
        fig.add_trace(go.Scatter(x=x_vals, y=y_taylor, mode='lines', name=f'테일러 급수 ({degree}차)'))

    fig.update_layout(
        title="테일러 급수 차수 비교",
        xaxis_title="x",
        yaxis_title="y",
        legend=dict(x=0, y=1),
        template="plotly_white"
    )

    fig.show()

taylor_series_comparison()