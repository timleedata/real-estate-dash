import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash('AtlMktDash')

df = pd.read_csv('static/data/rs_df.csv')
neighborhood_list = np.insert(arr=df['neighborhood'].unique(), obj=0, values='None selected', axis=0)

app.layout = html.Div([
    dcc.Dropdown(
        id='neighborhood-name',
        options=[{'label': name, 'value': name.lower()} for name in neighborhood_list],
        value='none selected'
    ),
    html.Div(id='dash-output')
])

@app.callback(
    dash.dependencies.Output('dash-output', 'children'),
    [dash.dependencies.Input('neighborhood-name', 'value')])
def callback_name(neighborhood_name):
    if neighborhood_name != "none selected":
        N = 500
        random_x = np.linspace(0, 1, N)
        random_y = np.random.randn(N)
    
        # Create a trace
        trace = go.Scatter(x=random_x,
                           y=random_y)
    
        data = [trace]
    
        layout = dict(title='',
                      yaxis=dict(zeroline=False, title='Average Value ($)',),
                      xaxis=dict(zeroline=False, title='Date', tickangle=0),
                      margin=dict(t=20, b=50, l=50, r=40),
                      height=350,
                     )
    
    
        fig = dict(data=data, layout=layout)
        line_graph = dcc.Graph(id='line-area-graph2', figure=fig, style={'display':'inline-block', 'width':'100%',
                                                                         'height':'100%;'})
        children = [line_graph]
    
        return children
    else:
        return "None selected\<br\>Pandas, numpy version: %s %s" %(pd.__version__, np.__version__)