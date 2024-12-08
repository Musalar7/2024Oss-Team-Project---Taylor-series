
"""
Sympy - Python library for symbolic mathematics
"""

__version__ = "0.1.0"


import sympy as sp

def taylor_series():
    """
    주어진 함수에 대해 테일러 급수를 계산하는 함수입니다.
    
    사용자가 입력한 함수의 테일러 급수를 지정된 중심점과 차수에서 계산합니다.
    입력된 함수는 `sympy`의 `sympify` 함수로 처리되어 수학식으로 변환됩니다.
    
    함수는 사용자가 원하는 함수, 급수의 중심, 그리고 차수를 입력받고,
    `sympy.series`를 사용하여 해당 함수의 테일러 급수를 구한 후 출력합니다.

    :returns: None
    :raises ValueError: 사용자가 입력한 함수가 유효한 수학식이 아닐 경우
    :param formula_input: 테일러 급수를 계산할 함수의 수학적 표현 (문자열)
    :type formula_input: str
    :param center: 테일러 급수의 중심
    :type center: float
    :param order: 테일러 급수의 차수 (몇 차까지 계산할지)
    :type order: int
    """
    formula_input = input("함수 입력: ")
    x = sp.Symbol('x')
    formula = sp.sympify(formula_input)

    center = float(input("급수의 중심 입력: "))
    order = int(input("급수의 차수 입력: "))
    
    taylor = sp.series(formula, x, center, order + 1).removeO()
    print("테일러 급수: {}". format(taylor))

    """
