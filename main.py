import requests as r
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

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


def prettify_data(result):
    data = result["data"]

    results = []

    for el in data:
        results.append(el["cells"])

    return {"data": results,
            "sql_query": result["executedSQLQuery"]}


token = get_token(username="samirsalman1997@gmail.com",
                  password="Askdatahackathon")

switch_workspace(token=token["access_token"])


@app.route('/query', methods=['POST'])
def query():
    print("Query Request")
    input_data = request.get_json()
    print(input_data)
    query = input_data["query"].strip()
    lang = input_data["lang"].strip()

    global token
    results = make_query(query=query,
                         lang=lang,
                         token=token["access_token"])

    results = prettify_data(result=results)

    if len(results) > 0:
        print(results)

    output = {
        "query": query,
        "lang": lang,
        "results": results["data"],
        "sql_query": results["sql_query"]
    }
    return jsonify(output)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
