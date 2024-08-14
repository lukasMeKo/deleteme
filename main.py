from oauthlib.oauth2 import BackendApplicationClient

from requests_oauthlib import OAuth2Session
from requests_oauthlib import OAuth2Session

import os
from time import time

token_endpoint = 'http://localhost:1024/login/azure'
client_id = os.environ["AZURE_CLIENT_ID"]
client_secret = os.environ["AZURE_CLIENT_SECRET"]

client = BackendApplicationClient(
    client_id=client_id,
)

oauth = OAuth2Session(client=client)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

token = oauth.fetch_token(
    token_url=token_endpoint,
    client_id=client_id,
    client_secret=client_secret,
)

print("got token")

def token_saver(new_token):
    print("refreshed token")

    token = new_token

oauth = OAuth2Session(
    client_id,
    token=token,
    auto_refresh_url=token_endpoint,
    token_updater=token_saver,
)

r = oauth.get("http://localhost:1024/")
print("get", r.status_code)

print("expiring token")
token['expires_at'] = time() - 10
oauth = OAuth2Session(
    client_id,
    token=token,
    auto_refresh_url=token_endpoint,
    token_updater=token_saver,
)

r = oauth.get("http://localhost:1024/")
print("get", r.status_code)

r = oauth.get("http://localhost:1024/")
print("get", r.status_code)
