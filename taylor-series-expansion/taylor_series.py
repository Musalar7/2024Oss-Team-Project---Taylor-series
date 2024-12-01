import sympy as sp

def taylor_series():
    formula_input = input("함수 입력: ")
    x = sp.Symbol('x')
    formula = sp.sympify(formula_input)


    taylor = sp.series(formula, x, 0, 6)
    print("테일러 급수: {}". format(taylor))
