"""Launcher for the WebApp.

The Main function performs 3 actions:
  - Initialise the Web Server (Dash). 
  - Callback retrieves data and plots it in the web. 
"""

from pkg_resources import resource_string
from mad9rodeo import update_data
import dash
from dash.dependencies import Input, Output
from dash import dcc, html 

def create_webapp():
    """ Builds a dash webapp. 
    Refresh parameter and 
    container is fixed. 
    """
    print("Creating render app...")
    app = dash.Dash(__name__)
    app.layout = html.Div(
        html.Div([
            html.Div(id = "container"),
            dcc.Interval(
                id='interval-component',
                interval=180*1000, # milliseconds
                n_intervals=0
            )
        ])
    )
    return app

if __name__ == '__main__':
    app = create_webapp()
    @app.callback(Output('container', 'children'),
              Input('interval-component', 'n_intervals'))
    def update_tables(n):
        """ Update data callback. """
        return update_data()
    app.run_server(debug=True)