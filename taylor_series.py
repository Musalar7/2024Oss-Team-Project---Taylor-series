import sympy as sp

def taylor_series():
    formula_input = input("함수 입력: ")
    x = sp.Symbol('x')
    formula = sp.sympify(formula_input

    center = float(input("급수의 중심 입력: "))
    order = int(input("급수의 차수 입력: "))

    
    taylor = sp.series(formula, x, center, order + 1).remove0()
    print("테일러 급수: {}". format(taylor))
