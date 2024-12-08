    def plot_comparison(self, center, orders, x_range=(-10, 10), num_points=500):
        x_vals = np.linspace(x_range[0], x_range[1], num_points)
        original_func = sp.lambdify(self.variable, self.function, modules="numpy")
        y_original = original_func(x_vals)

        fig = go.Figure()

        # Original function trace
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_original,
            mode='lines',
            name='Original Function',
            line=dict(color='blue'),
            customdata=np.stack([y_original, np.zeros_like(y_original)], axis=-1),  # [y_original, 0] 저장
            hovertemplate='x: %{x}<br>Original y: %{customdata[0]}<br>Difference: %{customdata[1]}<extra></extra>'  # 차이를 계산하여 표시
        ))

        for order in orders:
            taylor_expr = self.taylor_series(center, order)
            taylor_func = sp.lambdify(self.variable, taylor_expr, modules="numpy")
            y_taylor = taylor_func(x_vals)

            # 차이 계산 (절댓값 사용)
            diff = abs(y_original - y_taylor)  # 절댓값 차이 계산
            fig.add_trace(go.Scatter(
                x=x_vals,
                y=y_taylor,
                mode='lines',
                name=f'Taylor Series (Order {order})',
                line=dict(color='red'),
                customdata=np.stack([y_taylor, diff], axis=-1),  # [y_taylor, diff] 저장
                hovertemplate='x: %{x}<br>Taylor y: %{customdata[0]}<br>Difference: %{customdata[1]}<extra></extra>'  # 차이 표시
            ))

            area = self.diff_area(x_vals, y_original, y_taylor)
            for diff in area:
                fig.add_trace(diff)

        fig.update_layout(
            title=f"Taylor Series Approximation Comparison (Center: {center})",
            xaxis_title="x",
            yaxis_title="f(x)",
            legend_title="Functions",
            template="plotly_white",
        )

        fig.show()
