#!/usr/bin/python
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

from datetime import datetime

import pandas as pd

# получаем данные и трансформируем их
urbanization = pd.read_csv('data/urbanization.csv')
urbanization['Year'] = pd.to_datetime(urbanization['Year'], format = '%Y-%m-%d')

continents = ['Africa', 
              'Asia', 
              'Australia', 
              'Europe', 
              'North America', 
              'South America']
population_by_year = (urbanization.query('Entity.isin(@continents)')
                                  .groupby(['Entity', 'Year'])
                                  .agg({'Population': 'sum'})
                                  .reset_index())
                                  
population_by_year_lines = []
for continent in population_by_year['Entity'].unique():
    current = population_by_year.query('Entity == @continent')
    population_by_year_lines += [go.Scatter(x = current['Year'],
                                            y = current['Population'], 
                                          mode = 'lines',
                                          name = continent)]            

population_by_year_areas = []
for continent in population_by_year['Entity'].unique():
  current = population_by_year.query('Entity == @continent')
  population_by_year_areas += [go.Scatter(x = current['Year'],
                                          y = current['Population'], 
                                          mode = 'lines',
                                          stackgroup = 'one',
                                          name = continent)]  

population_by_year_scatter = []
for continent in population_by_year['Entity'].unique():
  current = population_by_year.query('Entity == @continent')
  population_by_year_scatter += [go.Scatter(x = current['Year'],
                                            y = current['Population'],
                                            mode = 'markers',
                                            name = continent)]    

data = [go.Bar(x = population_by_continent['Entity'], 
               y = population_by_continent['Rural Population'],              
               name = 'Сельское население'),
            go.Bar(x = population_by_continent['Entity'], 
               y = population_by_continent['Urban Population'],              
               name = 'Городское население')               
           ]

# задаём лейаут
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[  

    html.Label('График в виде линий:'),
    dcc.Graph(
        figure = {'data': population_by_year_lines, 
                  'layout': go.Layout(xaxis = {'title': 'Год'}, 
                                      yaxis = {'title': 'Население'})
                 },
        id = 'population_by_year_lines'
    ),   
    
    html.Label('График в виде областей с накоплением:'),
    dcc.Graph(
        figure = {'data': population_by_year_areas, 
                  'layout': go.Layout(xaxis = {'title': 'Год'}, 
                                      yaxis = {'title': 'Население'})
                 },
        id = 'population_by_year_areas'
    ),   

    html.Label('График в виде областей с точек:'),
    dcc.Graph(
        figure = {'data': population_by_year_scatter, 
                  'layout': go.Layout(xaxis = {'title': 'Год'}, 
                                      yaxis = {'title': 'Население'})
                 },
        id = 'population_by_year_scatter'
    ),      
  
])


if __name__ == '__main__':
    app.run_server(debug=True)