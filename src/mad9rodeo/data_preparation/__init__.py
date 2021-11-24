import json, math, requests, time
import pandas as pd
from pandas import DataFrame
from datetime import timedelta
from typing import Iterable

from mad9rodeo.data_preparation.merge import prepare_tables
from mad9rodeo.data_preparation.prep_cpts import split_cpts

def prepare_data(df_rodeo: DataFrame, 
                 df_demand: DataFrame
                 ) -> Iterable[DataFrame]:
    """Prepares the data. 

    Args: 
        df_rodeo: DataFrame containing 
            the Rodeo data.
        df_demand: DataFrame containg 
            the picking console data. 
    
    Returns: 
        Iterable of DataFrame 
        with multi/no multi demand 
        in the next 2 CPTs. 

    """
    df_out = prepare_tables(df_rodeo, df_demand)
    df_multi_cpt1, df_multi_cpt2, df_no_multi_cpt1, df_no_multi_cpt2 = split_cpts(df_out)
    return df_multi_cpt1, df_multi_cpt2, df_no_multi_cpt1, df_no_multi_cpt2