# auth.py


import requests, json, threading, webbrowser

from flask import Flask, request


CLIENT_ID = "YOUR_CLIENT_ID"

CLIENT_SECRET = "YOUR_CLIENT_SECRET" REDIRECT_URI = "http://localhost:3000/callback"

SCOPES = ["data:read", "data:write", "viewables:read"]


AUTH_URL = "https://developer.api.autodesk.com/authentication/v2/authorize"

TOKEN_URL = "https://developer.api.autodesk.com/authentication/v2/token"

TOKEN_FILE = "token_store.json"


app = Flask(__name__)

auth_code_holder = {}


@app.route('/callback')

def callback():

code = request.args.get('code')

if code:

auth_code_holder['code'] = code

return "✅ Auth successful. You may close this tab."

return "❌ Authorization failed."


def run_flask():

app.run(port=3000, debug=False, use_reloader=False)


def open_browser():

from urllib.parse import urlencode

params = {

"client_id": CLIENT_ID,

"response_type": "code",

"redirect_uri": REDIRECT_URI,

"scope": " ".join(SCOPES)

}

webbrowser.open(f"{AUTH_URL}?{urlencode(params)}")


def get_tokens(code):

data = {

"grant_type": "authorization_code",

"code": code,

"client_id": CLIENT_ID,

"client_secret": CLIENT_SECRET,

"redirect_uri": REDIRECT_URI

}

r = requests.post(TOKEN_URL, data=data)

r.raise_for_status()

return r.json()


if __name__ == "__main__":

threading.Thread(target=run_flask).start()

open_browser()


print("Waiting for login...")


while 'code' not in auth_code_holder:

pass


token_data = get_tokens(auth_code_holder['code'])


with open(TOKEN_FILE, 'w') as f:

json.dump(token_data, f)


print("✅ Token stored in token_store.json")
