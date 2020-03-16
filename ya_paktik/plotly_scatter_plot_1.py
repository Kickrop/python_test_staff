#!/usr/bin/python
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import pandas as pd
import math

# 
x = range(-100, 100, 1)
x = [x / 10 for x in x]

# задаём лейаут
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[  

    # формируем html
    html.H1(children = 'Тригонометрические функции'),

    # график
    dcc.Graph(
        figure =  {'data': [go.Scatter(x = pd.Series(x), 
                                       y = pd.Series([math.sin(x) for x in x]), 
                                       mode = 'lines', 
                                       name = 'sin(x)'),
                            go.Scatter(x = pd.Series(x), 
                                       y = pd.Series([math.cos(x) for x in x]), 
                                       mode = 'lines', 
                                       name = 'cos(x)')],
                   'layout': go.Layout(xaxis = {'title': 'x'},
                                       yaxis = {'title': 'y'})
                  },
        id = 'trig_func'
    ),      
])

# описываем логику дашборда
if __name__ == '__main__':
    app.run_server(debug=True)