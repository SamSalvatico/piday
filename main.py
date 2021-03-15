import requests as r
import json

ACCES_URL = 'https://api.askdata.com/security/domain/askdata/oauth/token'
WORKSPACE_URL = 'https://api.askdata.com/smartfeed/askdata/workspace/switch'
QUERY_URL = 'https://api.askdata.com/smartinsight/data/nl/result'


def get_token(username, password):
    res = r.post(ACCES_URL,
                 data={
                     "grant_type": "password",
                     "username": username,
                     "password": password
                 },
                 headers={
                     "Content-Type": "application/x-www-form-urlencoded",
                     "Authorization": "Basic ZmVlZDpmZWVk"
                 }
                 )
    print(res.text)
    return json.loads(res.text)


def switch_workspace(token):
    res = r.post(WORKSPACE_URL,
                 json={
                     "agent_slug": "pi_day"
                 },
                 headers={
                     "Content-Type": "application/json",
                     "Authorization": f"Bearer {token}"
                 }
                 )
    return res.text


def make_query(query, lang):
    res = r.post(WORKSPACE_URL,
                 json={
                     "nl": "Total cases by county", "language": "en"
                 },
                 headers={
                     "Content-Type": "application/json",
                     "Authorization": f"Bearer {token}"
                 }
                 )

    return res.text



token = get_token(username="samirsalman1997@gmail.com", password="Askdatahackathon")
switch_workspace(token=str(token["access_token"]))
print(make_query("", ""))
