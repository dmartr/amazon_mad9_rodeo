import time
from mad9rodeo.data_retriever import retrieve_data
from mad9rodeo.data_preparation import prepare_data
from mad9rodeo.plot_preparation import plot_tables

def update_data():
    start = time.time()
    df_rodeo, df_demand = retrieve_data()
    df_multi_cpt1, df_multi_cpt2, df_no_multi_cpt1, df_no_multi_cpt2 = prepare_data(df_rodeo, df_demand)
    print(f"Data pipeline done! Took {time.time() - start}")
    dash_tables = plot_tables(df_multi_cpt1, df_multi_cpt2, df_no_multi_cpt1, df_no_multi_cpt2)
    return dash_tables