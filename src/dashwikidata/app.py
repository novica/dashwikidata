from dash import Dash, dcc, html, Input, Output, State, dash_table
from .fct.functions import endpoint_url, get_results, wrangle_results, paste_query
import flask

server = flask.Flask(__name__) # define flask app.server
app = Dash(__name__,  server=server) # call flask server


app.layout = html.Div([
    html.H1('Wikidata dash test app'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Send code', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter code and press send code'),
    dash_table.DataTable(
        id = 'dt1'
    )

])


@app.callback(
    Output(component_id='container-button-basic', component_property='children'),
    Output(component_id='dt1', component_property='data'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='input-on-submit', component_property='value'),
    prevent_initial_call = True
)
def update_output(n_clicks, value):
     query = paste_query(value)
     results = get_results(endpoint_url=endpoint_url(), query=paste_query(value))
     names = wrangle_results(results=results)
     data = names.to_dict('rows')
     return query, data
