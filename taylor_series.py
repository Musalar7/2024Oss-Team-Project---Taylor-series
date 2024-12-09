"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"

import sympy as sp

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def taylor_series():
    """
    주어진 함수에 대해 테일러 급수를 계산하고, 시각화하는 함수입니다.

    사용자로부터 함수의 수학적 표현, 테일러 급수의 중심, 차수를 입력받아 해당 함수에 대해 
    테일러 급수를 계산하고, `TaylorSeriesPlotter` 클래스를 사용하여 원본 함수와 테일러 급수의 
    시각적 비교 그래프를 생성합니다.

    :param kind: 함수에 대한 수학적 표현 (예: sin(x), exp(x), log(1+x))
    :type kind: str
    :param center: 테일러 급수의 중심값 (예: 0, 1 등)
    :type center: float
    :param orders: 테일러 급수의 차수 목록 (예: [2, 4, 6])
    :type orders: list[int]

    :raise sp.SympifyError: 만약 입력된 함수가 `sympy`에서 해석할 수 없는 경우 발생
    :raise ValueError: 만약 숫자나 리스트 입력값에 오류가 있을 경우 발생

    :return: 없음. 대신 원본 함수와 테일러 급수의 시각적 비교 그래프를 생성하여 출력합니다.
    :rtype: None

    예시:
    1. `taylor_series()` 실행 후 함수로 `sin(x)` 입력
    2. 중심을 `0`으로 입력하고, 차수 `[2, 4, 6]` 입력 시 `sin(x)`의 테일러 급수 2차, 4차, 6차 근사값이 시각적으로 표시됩니다.
    """
    try:
        # 사용자 입력 받기
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
