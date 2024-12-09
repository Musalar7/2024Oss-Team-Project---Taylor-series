"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def get_random_ingredients(self, center=0, orders=[2, 4, 6], x_range=(-10, 10), num_points=500):
    """
    :param center: 테일러 급수 근사 중심 (기본값: 0)
    :param orders: 테일러 급수 차수 (기본값: [2, 4, 6])
    :param x_range: x값의 범위 (기본값: (-10, 10))
    :param num_points: x값을 생성할 점의 수 (기본값: 500)

    예시:
    1. `taylor_series()` 실행 후 함수로 `sin(x)` 입력
    2. 중심을 `0`으로 입력하고, 차수 `[2, 4, 6]` 입력 시 `sin(x)`의 테일러 급수 2차, 4차, 6차 근사값이 시각적으로 표시됩니다.
    """
