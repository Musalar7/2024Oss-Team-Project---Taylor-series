Codes
=====

1. ** 일반 함수를 테일러 급수로 변환 **
------------------------

원하는 함수를 사용자에게 제공받고, 이 함수를 테일러 급수로 변환시키기 위해 `taylor_series()` 함수를 이용할 수 있습니다.

이 함수는 사용자로부터 함수의 수학적 표현, 급수의 중심, 차수를 입력받아, 주어진 함수에 대해 해당 중심과 차수에서의 테일러 급수를 계산하여 출력합니다.

.. autofunction:: taylor_series.taylor_series


2. ** 테일러 급수의 그래프 생성 **
--------------------------

첫 번째 단계에서 만든 테일러 급수를 그래프의 형태로 변환시키기 위해 plotly 라이브러리를 이용할 수 있습니다.

이 함수는 지정된 차수의 테일러 급수를 계산하고, 원본 함수와 해당 급수의 차수에 대한 근사값을
시각적으로 비교하는 Plotly 그래프를 생성합니다.

.. autofunction:: taylor-seriesgap.TaylorSeriesPlotter.plot_comparison


3. **Generate the graph of the Taylor series**
---------------------

To convert the Taylor series created in the first step into a graph, you can use the `plot()` function. This function calculates the Taylor series at the given center and order and generates a graph that visually compares the original function and the Taylor series using Plotly.
