"""
Sympy - Python library for symbolic mathematics
"""

__version__ = "0.1.0"

import sympy as sp

def taylor_series():
    """
    주어진 함수에 대해 테일러 급수를 계산하고 그 결과를 시각화하는 함수입니다.

    이 함수는 사용자로부터 함수의 수학적 표현, 테일러 급수의 중심, 그리고 차수를 입력받아 
    해당 함수의 테일러 급수를 계산하고, `TaylorSeriesPlotter` 클래스를 사용하여 원본 함수와 
    테일러 급수를 시각적으로 비교하는 그래프를 생성합니다.

    사용자 입력:
    - 함수: 수학적으로 표현된 함수 (예: sin(x), exp(x), log(1+x))
    - 중심: 테일러 급수의 전개 중심 (예: 0, 1 등)
    - 차수: 테일러 급수의 차수 목록 (예: 2, 4, 6)

    예외 처리:
    - 입력된 함수가 `sympy`에서 해석할 수 없는 경우, `SympifyError` 발생
    - 숫자나 리스트 입력값에 오류가 있을 경우 `ValueError` 발생

    반환 값:
    - 함수의 출력값은 없으며, 그래프를 생성하여 시각적으로 표시합니다.

    예시:
    1. `taylor_series()`를 실행하고 함수로 `sin(x)`를 입력
    2. 중심을 `0`으로 입력하고, 차수 `2, 4, 6`을 입력하면
       `sin(x)`의 테일러 급수 2차, 4차, 6차 근사값이 시각적으로 표시됩니다.
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
