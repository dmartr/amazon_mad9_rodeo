import requests, json
import pandas as pd

def request_demand(auth, demandId):
    url = f"https://picking-console.eu.picking.aft.a2z.com/api/fcs/MAD9/pickdemands/consumertype/CUSTOMER_SHIPMENT/consumerreferenceid/{shipment_id}"
    session = requests.Session()
    request = session.get(url, 
                verify=False, 
                auth=auth
                )
    try:
        demandId = json.loads(request.text)["demandId"] 
    except:
        print(request.text)
    return 
    url = 'https://picking-console.eu.picking.aft.a2z.com/api/fcs/MAD9/pickactions/history'
    data = '{"demandIds":["' + demandId + '"]}'
    request = session.post(url, 
                verify=False, 
                data = data,
                headers = {
                        'Accept':'application/json',
                        'Content-Type':'application/json',
                        'Content-Length': str(len(data))
                    }
                )
    return request

def prepare_demand(request):                     
  try:                      
    return (
        pd.DataFrame
                .from_records(
                    json.loads(request.text)["demandActions"])
                    [
                        [
                            "consumerReferenceId", 
                            "fcSku", 
                            "destScannableId", 
                            "sourceScannableId"
                        ]
                    ]
        .dropna()
    )

  except:
    print(shipment_id)
    print(request.text)
    return 

def get_demand(auth, demandId): 
    return prepare_demand(request_demand)

def get_in_transit(auth, assigments):
    dfs = []
    for assigment_id in assigments:
        dfs.append(get_demand(auth, assigment_id))
    return pd.concat(dfs)