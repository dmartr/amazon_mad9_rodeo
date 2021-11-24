from pandas import DataFrame
from mad9rodeo.plot_preparation.build_html import build_children, build_div
from mad9rodeo.plot_preparation.prep import parse_cpts

def plot_tables(df_multi_cpt1: DataFrame, 
                df_multi_cpt2: DataFrame, 
                df_no_multi_cpt1: DataFrame, 
                df_no_multi_cpt2: DataFrame):
    # Get cpts from the dataframe.
    cpt1, cpt2 = parse_cpts(df_multi_cpt1, df_multi_cpt2, df_no_multi_cpt1, df_no_multi_cpt2)
    # Drops the CPT columns from all the dataframes
    df_multi_cpt1 = df_multi_cpt1.drop(columns=["CPT"])
    df_multi_cpt2 = df_multi_cpt2.drop(columns=["CPT"])
    df_no_multi_cpt1 = df_no_multi_cpt1.drop(columns=["CPT"])
    df_no_multi_cpt2 = df_no_multi_cpt2.drop(columns=["CPT"])    
    # Builds the html required for the web
    data_cpt1 = build_children(cpt1, "table_multi_cpt1", 'table_nomulti_cpt1', 
                               df_multi_cpt1, df_no_multi_cpt1)
    data_cpt2 = build_children(cpt2, "table_multi_cpt2", 'table_nomulti_cpt2', 
                               df_multi_cpt2, df_no_multi_cpt2)
    return [
        build_div("tables-cpt1", data_cpt1), 
        build_div("tables-cpt2", data_cpt2)
    ]