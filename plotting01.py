import plotly
plotly.offline.init_notebook_mode(connected=True)
# use offline mode to avoid initial registration
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 10]}
trace0
plotly.offline.iplot([trace0])
