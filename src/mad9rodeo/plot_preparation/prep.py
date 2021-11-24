from pandas import DataFrame
from mad9rodeo.data_preparation.prep_cpts import extract_cpt

def parse_cpts(df_multi_cpt1, df_multi_cpt2, df_no_multi_cpt1, df_no_multi_cpt2):
    """ Extracts the CPT value 
    from any given dataframe.
    """
    cpt1 = extract_cpt(df_multi_cpt1)
    cpt2 = extract_cpt(df_multi_cpt2) 
    if cpt1 == '':
        cpt1 = extract_cpt(df_no_multi_cpt1)
    if cpt2 == '':
        cpt2 = extract_cpt(df_no_multi_cpt2)
    return cpt1, cpt2



  
