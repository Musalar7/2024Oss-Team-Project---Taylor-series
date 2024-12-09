"""
Sympy - Python library for symbolic mathematics
"""

__version__ = "0.1.0"

import sympy as sp

def taylor_series():
    try:
        function_input = input("함수를 입력하세요 (예: sin(x), exp(x), log(1+x)): ")
        function = sp.sympify(function_input)  # 함수 입력 처리

        center_input = input("테일러 급수의 중심을 입력하세요: ")
        center = float(center_input)  # 중심 입력 처리

        orders_input = input("급수의 차수를 입력하세요 (예: 2, 4, 6): ")
        orders = list(map(int, orders_input.split(',')))  # 차수 입력 처리

        plotter = TaylorSeriesPlotter(function)
        plotter.plot_comparison(center=center, orders=orders)

    except (sp.SympifyError, ValueError) as e:
        print(f"오류 발생: {e}. 입력 값을 확인하고 다시 시도해 주세요.")
