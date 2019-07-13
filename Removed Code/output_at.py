import plotly
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)


def output_at(list_of_terms, x_values):

    if type(x_values) == int:
        result = ((list_of_terms[0][0]) * (x_values**list_of_terms[0][1])-11)
        return result

    else:
        results = []
        x_list_map = list(range(len(x_values)))
        for every_x in x_list_map:
            results.append(
                (list_of_terms[0][0]) * (x_values[every_x]**list_of_terms[0][1])-11)

        return results


three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
x_values = list(range(-30, 30, 1))
y_values = list(output_at(three_x_squared_minus_eleven, x_values))

iplot([{"x": x_values, "y": y_values}])
