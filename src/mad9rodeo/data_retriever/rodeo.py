import pandas as pd
import requests

PROCESS_LIST = [
    "PPExceptionNonCon",
    "PPMultiMedium",
    "PPMultiWrap",
    "PPMultiXLarge",
    "PPMultiXLargePT",
    "PPNonCon",
    "PPNonConPT", 
    "PPNonConPackTL",
    "PPPetfood",
    "PPSingleMedium",
    "PPSingleWrap",
    "UnassignedProcessPath"
  ]

def get_rodeo_url():
  file_url = r"https://rodeo-dub.amazon.com/MAD9/ItemListCSV?"
  process_url = ",".join(PROCESS_LIST)
  columns_url = f"_enabledColumns=on&enabledColumns=OUTER_SCANNABLE_ID&ProcessPath={process_url}"
  url_end = "&WorkPool=PickingPicked&ExSDRange.quickRange=ALL&Excel=true&shipmentType=CUSTOMER_SHIPMENTS"
  return file_url+columns_url+url_end

def request_rodeo(auth):
  request = requests.get(
    get_rodeo_url(),
    verify=False,
    auth=auth 
  )
  return request

def prepare_rodeo(request):
    del_cols = [
      "Condition", 
      "Ship Method", 
      "Ship Option", 
      "Pick Priority"
      ]
    # HTML to Pandas DataFrame
    df_rodeo = pd.read_html(request.content)[0]
    # Drop unused columns
    df_rodeo = df_rodeo.drop(columns=del_cols)
    # Filter relevant data 
    df_rodeo = (
        df_rodeo[
            ~df_rodeo["Outer Scannable ID"]
            .str
            .startswith(("ws", "rd", "dz-P-Pack", "dz-P-Multis", "dz-P-OB-Pet"))
            ]
        )
    df_rodeo = df_rodeo[df_rodeo["Work Pool"] != "PickingPickedInProgress"]
    return df_rodeo

def get_rodeo_data(auth):
    request = request_rodeo(auth)
    df = prepare_rodeo(request)
    return df

def get_assignments(df_rodeo):
    df_f =  (df_rodeo[df_rodeo["Work Pool"] == "PickingPickedInTransit"]
                .sort_values(["Scannable ID", "Dwell Time (hours)"])
                .groupby("Scannable ID")
                .first()
                .reset_index()
                )
    assigments = df_f.groupby("Scannable ID").first()["Shipment ID"].unique().tolist()
    return assigments