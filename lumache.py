
__version__ = "0.1.0"

def get_random_ingredients(self, center=0, orders=[2, 4, 6], x_range=(-10, 10), num_points=500):
    """
    :param center: 테일러 급수 근사 중심 (기본값: 0)
    :param orders: 테일러 급수 차수 (기본값: [2, 4, 6])
    :param x_range: x값의 범위 (기본값: (-10, 10))
    :param num_points: x값을 생성할 점의 수 (기본값: 500)

    **작동 방식**:
       - `plot_comparison` 함수는 주어진 함수의 **테일러 급수**를 계산하고, 원본 함수와 해당 급수의 차수에 대한 근사값을 비교하는 Plotly 그래프를 생성합니다.
       
       - 사용자가 지정한 `center` (테일러 급수의 중심값)와 `orders` (차수 목록)에 대해 **SymPy**를 사용해 테일러 급수를 계산하고, `x_vals`를 기준으로 근사값을 생성합니다.
       
       - 생성된 그래프에서는 원본 함수와 각 차수의 테일러 급수가 다른 색으로 표시되며, 차수별 테일러 급수와 원본 함수의 근사 차이를 시각적으로 비교할 수 있습니다.
