# Class 내부, 오차 표시
def diff_area(self, x_vals, y_original, y_taylor):
        error = y_original - y_taylor
        area = []

        for i in range(1, len(x_vals)):  
            x_area = [x_vals[i-1], x_vals[i], x_vals[i], x_vals[i-1]]
            y_area = [y_taylor[i-1], y_taylor[i], y_original[i], y_original[i-1]]

            
            if error[i] > 0:
                color = "rgba(0, 0, 255, 0.2)"
            else:
                color = "rgba(255, 0, 0, 0.2)"

            area.append(go.Scatter(x=x_area, y=y_area, fill='toself', mode='lines', line_width=0, fillcolor = color, showlegend = False))

        return area

# for order in orders: 구문 안 제일 밑에 삽입
area = self.diff_area(x_vals, y_original, y_taylor)
            for diff in area:
                fig.add_trace(diff)
