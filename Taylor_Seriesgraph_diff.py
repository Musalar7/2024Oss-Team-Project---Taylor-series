# Class 내부, 오차 표시
def diff_area(self, x_vals, y_original, y_taylor):
        """
        
        :param x_vals: 함수 그래프의 x값 목록
        :param y_original: 원본 함수의 y값
        :param y_taylor: 테일러 급수의 y값
              
        :return: 차이 영역을 나타내는 **Plotly 그래프 객체** 목록


        **작동 방식**:
           - 함수는 각 `x` 값에 대해, 원본 함수와 테일러 급수 간의 차이(오차)를 계산합니다.
           - `y_original - y_taylor` 값이 양수일 경우 해당 구간을 파란색으로, 음수일 경우 빨간색으로 채웁니다.
           - 이 차이를 그래프 영역으로 강조하고, 이를 Plotly Scatter 객체로 반환하여 `plot_comparison`에서 시각적으로 추가합니다.

        
        **작동 예시**:
           x_vals = np.linspace(-10, 10, 500)
           y_original = np.sin(x_vals)
           y_taylor = np.taylor_series(x_vals, center=0, order=2)

           area = diff_area(x_vals, y_original, y_taylor)
           for diff in area:
               fig.add_trace(diff)
               
           """
