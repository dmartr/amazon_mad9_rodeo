from pandas import DataFrame
from dash import dash_table, dcc, html 
from mad9rodeo.plot_preparation.datatable import build_datatable
from typing import Iterable, Type

def build_children(cpt: str, 
                   id_multi: str, 
                   id_no_multi: str, 
                   df_multi: DataFrame, 
                   df_no_multi: DataFrame
                   ) -> Iterable:
    """ Build an iterable containg a title and 
    two datables to plot the data. """
    return [
            html.H3(children=f'CPT {cpt}h'),
            build_datatable(id_multi, df_multi),
            build_datatable(id_no_multi, df_no_multi)
            ]

def build_div(name_id: str, 
              children: Iterable):
    """ Build a div with a 
    given id and children.
    """
    return html.Div(id = name_id, children = children)