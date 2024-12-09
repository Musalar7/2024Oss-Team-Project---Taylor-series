"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def get_random_ingredients(kind=None):
    """
    :param function: 수학적 표현으로 입력된 함수
    :type function: str
    :param center: 테일러 급수의 전개 중심
    :type center: int
    :param orders: 테일러 급수의 차수 목록
    :type orders: list[int]

    :return: None
    :rtype: None

    예시:
    1. `taylor_series()` 실행 후 함수로 `sin(x)` 입력
    2. 중심을 `0`으로 입력하고, 차수 `[2, 4, 6]` 입력 시 `sin(x)`의 테일러 급수 2차, 4차, 6차 근사값이 시각적으로 표시됩니다.
    """
