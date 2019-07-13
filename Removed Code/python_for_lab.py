import plotly
import pandas


file_name = 'C:/Users/GILOR/Desktop/coding_projects/cities.xlsx'
travel_df = pandas.read_excel(file_name)
cities = travel_df.to_dict('records')
# plotly.offline.init_notebook_mode(connected=True)


# creating a list of names. god bless internet.
city_names = [name['City'] for name in cities]
city_indices = list(range(len(cities)))  # list of numbers to iterations
names_and_ranks = []
city_populations = []
city_areas = []
num_index = 0


# create a list and rank for every city
for city_indices in city_names:
    # why does this list me individually eachh city? why does [0,1,2 ...] turns to the city names, how do I keep it as integers?
    names_and_ranks.append(f"{num_index + 1}. {city_indices}")


for city_indices in cities:
    # create a list with all the populations
    city_populations.append(city_indices['Population'])
    # create a list of all areas
    city_areas.append(city_indices['Area'])


trace_populations = {'x': names_and_ranks, 'y': city_populations,
                     'text': names_and_ranks, 'type': 'bar', 'name': 'populations'}

plotly.offline.init_notebook_mode(connected=True)
plotly.offline.iplot([trace_populations])

trace_areas = {'x': names_and_ranks, 'y': city_areas,
               'text': names_and_ranks, 'type': 'bar', 'name': 'areas'}

plotly.offline.init_notebook_mode(connected=True)
plotly.offline.iplot([trace_areas])
