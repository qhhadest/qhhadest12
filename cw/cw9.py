import requests

response = requests.get("https://coinmarketcap.com/")

response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem in response_parse:
    if parse_elem.startswith('$'):