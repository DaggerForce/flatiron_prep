# pip install pandas
# python -m pip install --upgrade pip

import pandas
travel_df = pandas.read_excel('./cities.xlsx')
cities = travel_df.to_dict('records')
cities[0]
# Note that the `keys()` function returns a `dict_keys` object. It's a little tricky to work with that type of object, so let's coerce it into a list.
list(cities[0].keys())
list(cities[0].values())  # similar to the 'keys' this is the value of each key

# philadelphia = {'City': 'Philadelphia'} - how we learnt to create dictionarys
# pittsburgh = dict(city='Pittsburgh')- another possible way.
# dict(city="Las Vegas", state="Nevada")
