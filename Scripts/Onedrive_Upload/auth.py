# auth.py
import msal

# Replace with your Azure Credentials
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET_ID = 'your_client_secret_here'
TENANT_ID = 'your_tenant_id_here'
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

# MSAL Authentication to get access token
def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET_ID,
    )
    result = app.acquire_token_for_client(scopes=SCOPE)  # Use client credentials to get access token
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception(f"Could not get the access token needed: {result.get('error_description')}")
