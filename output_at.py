def output_at(list_of_terms, x_values):
    results = []
    x_list_map = list(range(len(x_values)))
    term1 = list_of_terms[0]

    for every_x in x_list_map:
        results.append((term1[0])*(x_values[every_x]**term1[1])-11)

    return results


three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
x_values = list(range(-30, 30, 1))
y_values = list(output_at(three_x_squared_minus_eleven, x_values))
