
"""
plotly - python library for making graphs
"""
class TaylorSeriesPlotter:
    def __init__(self, function, variable='x'):
        self.function = sp.sympify(function)
        self.variable = sp.Symbol(variable)

    def taylor_series(self, center, order):
        return sp.series(self.function, self.variable, center, order + 1).removeO()

    def plot(self, center, order, x_range=(-10, 10), num_points=500):
        """
        Plot the graph of the original function and its Taylor series approximation.
        This plots the graph of the Taylor series created in step 1.
        
        :param center: The center of expansion for the Taylor series.
        :type center: float
        :param order: The order (degree) of the Taylor series.
                      This determines how many terms of the series are included in the approximation.
        :type order: int
        :param x_range: The range of x-values over which the functions will be plotted.
                         This is given as a tuple of the form (min, max).
                         Default is (-10, 10).
        :type x_range: tuple[float, float], optional
        :type num_points: int, optional
        :return: None
        """
