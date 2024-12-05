        diff = y_original - y_taylor
        diff_area = 0.5
        
        for i in range(len(diff)):
            if diff[i] > 0:
                fig.add_trace(go.Scatter(
                    x=[x_vals[i]], y=[y_original[i]],
                    mode= "markers",
                    color = "blue", size = 4
                ))
            else:
                fig.add_trace(go.Scatter(
                    x=[x_vals[i]], y=[y_original[i]],
                    mode="markers",
                    color = "red", size = 4
                ))

        
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=x_vals, y=error, mode='lines', name="Diff Graph"))

        fig2.update_layout(
            title="Diff Graph",
            xaxis_title="x",
            yaxis_title="Difference",
        )

        
        fig2.show()             # fig.show() 와 함께 그래프를 표시
