import requests
import json

backend = 'https://b493-142-185-241-49.ngrok.io'

payload = json.dumps({
  "start_lat": 22,
  "start_lon": 33,
  "end_lat": 55,
  "end_lon": 66
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", backend, headers=headers, data=payload)