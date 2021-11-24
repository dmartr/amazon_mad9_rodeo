from pandas import DataFrame
from typing import Type
from dash.dash_table import DataTable

def build_datatable(table_id: str, 
                    df: DataFrame):
    """ Builds a standard Dash datatable 
    used for plotting dataframes. """
    return DataTable(
        id=table_id,
        columns=[{"name": i, "id": i} for i in df.columns],
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in df.columns
        ],
        style_header={
            'backgroundColor': 'grey',
            'fontWeight': 'bold'
        },
        style_as_list_view=True,
        data=df.to_dict('records')
    )
