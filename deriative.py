def output_at(list_of_terms, x_values):
    if type(x_values) == int:
        result = ((list_of_terms[0][0]) * (x_values) + (list_of_terms[1][0]))
        return result

    else:
        results = []
        x_list_map = list(range(len(x_values)))
        for every_x in x_list_map:
            results.append(
                (list_of_terms[0][0]) * (x_values[every_x]) + (list_of_terms[1][0]))

        return results


def deriative_at(list_of_terms, x_value, delta_x):
    f_x = output_at(list_of_terms, x_value)
    f_x_plus_delta_x = output_at(list_of_terms, (x_value + delta_x))
    deriative = ((f_x_plus_delta_x) - (f_x))/delta_x
    return round(deriative)


four_x_plus_fifteen = [(4, 1), (15, 0)]
