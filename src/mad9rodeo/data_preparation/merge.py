import pandas as pd
from pandas import DataFrame

MERGED_COLS = [
    "Scannable ID", 
    "Expected Ship Date", 
    "Outer Scannable ID", 
    "Process Path", 
    "Dwell Time (hours)"
    ]

def filter_workpool(df: DataFrame, 
                    status: str
                    ) -> DataFrame:
    """Filters the work pool and sorts 
    the DataFrame by ID and time. 
    """
    return (
        df[df["Work Pool"] == status]
        .sort_values(["Scannable ID", "Dwell Time (hours)"])
        .groupby("Scannable ID")
        .first()
        .reset_index()
        )

def prepare_tables(df_rodeo: DataFrame, 
                   df_demand: DataFrame
                   ) -> DataFrame:
    """ Merges the rodeo and picking 
    console data and prepares it.
    """
    df_merged = df_rodeo.merge(df_demand, 
                               left_on=["Scannable ID"], 
                               right_on="destScannableId", 
                               how="inner")
    df_in_transit = filter_workpool(df_merged, "PickingPickedInTransit")
    df_atDest = filter_workpool(df_merged, "PickingPickedAtDestination")
    df_final = pd.concat([df_atDest, df_in_transit])
    df_final["Outer Scannable ID"] = (
        df_final
        .apply(lambda row: row["sourceScannableId"] if row["Outer Scannable ID"] == "cvAtPM00002" else row["Outer Scannable ID"], axis=1))
    df_final["Expected Ship Date"] = pd.to_datetime(df_final["Expected Ship Date"])
    df_final = df_final[MERGED_COLS].sort_values("Expected Ship Date", ascending=True)
    return df_final