import plotly
plotly.tools.set_credentials_file(username='craigwendel', api_key='RXUoyJhDkztUKAqSwLD5')

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('2015-nfl-combine-results.csv', error_bad_lines=False)

trace = go.Scattergl(
    x = df['name'],
    y = df['bench'],
    mode = 'markers',
    marker = dict(
        color = '#3498db',
        line = dict(width = 2)
    )
)

layout = go.Layout(
    title='NFL Combine Bench Press Results, 2015',
)

data = [trace]
py.plot(data, layout, filename='nfl-combine-benchpress')
