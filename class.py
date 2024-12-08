
"""
plotly - python library for making graphs
"""
import sympy as sp
import numpy as np
import plotly.graph_objects as go

class TaylorSeriesPlotter:
    """
    주어진 함수에 대해 테일러 급수를 계산하고, 원본 함수와 테일러 급수를 시각화하는 클래스입니다.
    
    이 클래스는 사용자가 제공한 함수에 대해 지정된 중심과 차수에서 테일러 급수를 계산하고,
    Plotly를 사용하여 원본 함수와 테일러 급수의 근사치를 그래프 형식으로 출력합니다.
    """

    def __init__(self, function, variable='x'):
        """
        TaylorSeriesPlotter 클래스의 생성자.

        :param function: 테일러 급수를 계산할 수학적 함수
        :type function: str 또는 sympy expression
        :param variable: 함수에서 변수로 사용할 기호 (기본값은 'x')
        :type variable: str, optional
        """
        self.function = sp.sympify(function)
        self.variable = sp.Symbol(variable)

    def taylor_series(self, center, order):
        """
        주어진 함수에 대해 특정 중심과 차수에서 테일러 급수를 계산합니다.

        :param center: 테일러 급수의 중심
        :type center: float
        :param order: 테일러 급수의 차수
        :type order: int
        :returns: 테일러 급수의 근사식
        :rtype: sympy expression
        """
        return sp.series(self.function, self.variable, center, order + 1).removeO()

    def plot(self, center, order, x_range=(-10, 10), num_points=500):
        """
        원본 함수와 해당 함수의 테일러 급수를 시각화합니다.

        주어진 중심과 차수에서의 테일러 급수를 계산하고, Plotly를 사용하여 원본 함수와 급수의 근사치를 비교하는 그래프를 생성합니다.

        :param center: 테일러 급수의 중심
        :type center: float
        :param order: 테일러 급수의 차수
        :type order: int
        :param x_range: 그래프에서 사용할 x 값의 범위 (기본값은 -10에서 10까지)
        :type x_range: tuple, optional
        :param num_points: 그래프에서 사용할 데이터 포인트의 수 (기본값은 500)
        :type num_points: int, optional
        :returns: None
        :raises ValueError: x_range의 크기나 num_points가 유효하지 않은 경우
        """
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
