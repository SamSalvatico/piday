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
    return res.json()


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


def make_query(query, lang, token):
    res = r.post(QUERY_URL,
                 json={
                     "nl": query,
                     "language": lang
                 },
                 headers={
                     "Content-Type": "application/json",
                     "Authorization": f"Bearer {token}"
                 }
                 )

    return res.json()


def prettify_data(data):
    data = result["data"]

    results = []

    for el in data:
        results.append(el["cells"])
    return results


token = get_token(username="samirsalman1997@gmail.com",
                  password="Askdatahackathon")

switch_workspace(token=token["access_token"])
result = make_query(query="Total cases today", lang="en", token=token["access_token"])

result = prettify_data(result)

if len(result) > 0:
    print(result[0])

