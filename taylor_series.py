"""
Sympy - Python library for symbolic mathematics
"""

__version__ = "0.1.0"

import sympy as sp

def taylor_series():
    """
    :param formula_input: 테일러 급수를 계산할 함수의 수학적 표현 (문자열)
    :type formula_input: str
    :param center: 테일러 급수의 중심
    :type center: float
    :param order: 테일러 급수의 차수 (몇 차까지 계산할지)
    :type order: int
    :returns: None

    예시:
    >>> taylor_series()
    함수 입력: sin(x)
    급수의 중심 입력: 0
    급수의 차수 입력: 4
    테일러 급수: x - x**3/6 + O(x**5)
    """
    formula_input = input("함수 입력: ")
    x = sp.Symbol('x')
    formula = sp.sympify(formula_input)

    center = float(input("급수의 중심 입력: "))
    order = int(input("급수의 차수 입력: "))
    
    taylor = sp.series(formula, x, center, order + 1).removeO()
    print("테일러 급수: {}". format(taylor))
