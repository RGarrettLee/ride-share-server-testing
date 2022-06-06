import requests
import json

backend = 'https://d979-142-185-241-49.ngrok.io'

payload = json.dumps({
  'origin': {
      "city": "Toronto",
      "country": "CA",
      "postal_code": "M4W 1V1",
      "street": "175 Crescent Road"
  },
  'dest': {
    'city': 'Toronto',
    'country': 'CA',
    'postal_code': 'M4T 1P4',
    'street': '340 Saint Clair Avenue East'
  }
})

headers = {
  'Content-Type': 'application/json'
}

#response = requests.request("POST", backend, headers=headers, data=payload)

data = requests.get('{}/data'.format(backend)).json()

print(data)