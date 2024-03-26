import requests

# Substitua 'your-token-here' pelo seu GitHub PAT
token2 = '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'

headers = {'Authorization': f'token {token}'}

response = requests.get('https://api.github.com/user', headers=headers)

print(response.json())