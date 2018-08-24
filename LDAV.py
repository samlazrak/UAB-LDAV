import dash
import dash_core_components as dcc
import dash_html_components as html
import json

# Dash wants .json, had to do some work to get the data there.
# .axgt -> .csv -> .sqlite -> .json
# Could not go directly from .axgt (tab-delim) to .json due to memory limitations, using .sqlite db as middleman
# .axgt -> .csv because inserting into sqlite database is simpler with .csv

X = []
Y = []

with open('./data/axondata.json') as json_file:
  data = json.load(json_file)
  for element in data:
    X.append(element['(ime(s))'])
    Y.append(element['(race#1(pA))'])

app = dash.Dash()

app.layout = html.Div(children=[
  html.H1('LDAP Dash'),
  dcc.Graph(id='LDAP',
            figure={
              'data': [
                {'x': X,
                 'y': Y,
                 'type': 'line',
                 'name': 'boats'},
              ],
              'layout': {
                'title': 'LDAP Dash Example'
              }
            })
])

if __name__ == '__main__':
  app.run_server(debug=True)
