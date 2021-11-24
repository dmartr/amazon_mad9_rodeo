from mad9rodeo.data_retriever.rodeo import get_rodeo_data, get_assignments
from mad9rodeo.data_retriever.picking import get_in_transit
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from requests_kerberos import HTTPKerberosAuth, REQUIRED, OPTIONAL
KERBEROS_AUTH = HTTPKerberosAuth(mutual_authentication=OPTIONAL)

def retrieve_data():
    print("Retrieving data from rodeo...")
    df_rodeo = get_rodeo_data(KERBEROS_AUTH)
    assigments = get_assignments(df_rodeo)
    print("Retrieving data from picking console...")
    df_demand = get_in_transit(KERBEROS_AUTH, assigments)
    return df_rodeo, df_demand