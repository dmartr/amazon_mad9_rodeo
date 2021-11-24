import pandas as pd
from pandas import DataFrame
from mad9rodeo.data_preparation.formatter import format_HM

RENAMED_COLS = {
    "Scannable ID": "Container", 
    "Expected Ship Date": "CPT", 
    "Outer Scannable ID": "Location",
    "Dwell Time (hours)": "Dwell"
    }

def filter_cpt(df: DataFrame, 
               cpt: str
               ) -> DataFrame:
    """ Filter the dataframe 
    given a CPT. """
    return df[df["CPT"] == cpt]

def filter_process(df: DataFrame, 
                   process: str
                   ) -> DataFrame:
    """ Filter the dataframe by 
    multi/nomulti process."""
    cond = df["Process Path"].str.startswith("PPMulti")
    if process == "multi":
        df = df[cond]
    else: 
        df = df[~cond]
    return (
        df
        .sort_values("Dwell", ascending=False)
        .reset_index(drop=True)
        )

def format_dwell(df: DataFrame) -> DataFrame:
    return df["Dwell"].apply(lambda l: format_HM(l))

def split_cpts(df: DataFrame) -> DataFrame:
    """ Splits a given dataframe based on 
    the CPT and multi/no-multi procedure.
    """
    cpts = df["Expected Ship Date"].drop_duplicates()[:2].tolist()
    df = df.rename(columns=RENAMED_COLS)
    df_cpt1 = filter_cpt(df, cpts[0])
    df_cpt2 = filter_cpt(df, cpts[1])
    df_multi_cpt1 = filter_process(df_cpt1, "multi")
    df_multi_cpt2 = filter_process(df_cpt2, "multi")
    df_no_multi_cpt1 = filter_process(df_cpt1, "nomulti")
    df_no_multi_cpt2 = filter_process(df_cpt2, "nomulti")
    df_multi_cpt1 = format_dwell(df_multi_cpt1)
    df_multi_cpt2 = format_dwell(df_multi_cpt2)
    df_no_multi_cpt1 = format_dwell(df_no_multi_cpt1)
    df_no_multi_cpt2 = format_dwell(df_no_multi_cpt2)
    return df_multi_cpt1, df_multi_cpt2, df_no_multi_cpt1, df_no_multi_cpt2

def extract_cpt(df: DataFrame) -> str:
    """ Extracts the CPT from 
    the dataframe. 
    """
    if df.shape[0] > 0: 
        return (pd.to_datetime(
                    df
                    .CPT
                    .unique()[0]
                    )
                    .strftime('%Y-%m-%d %H:%M')
                )
    else: 
        return ''