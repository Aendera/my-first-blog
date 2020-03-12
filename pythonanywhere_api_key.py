import requests
username = 'Aendera'
token = 'e1a9850a88d4465da93c846348a82b7271e551d7'

response = requests.get(
  'https://eu.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
      username=username
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('CPU quota info:')
  print(response.content)
else:
  print('Got unexpected status code {}: {!r}'.format(
  response.status_code, response.content))
