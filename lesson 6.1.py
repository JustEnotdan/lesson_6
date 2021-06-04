from requests import get, utils
import json

response = utils.get_unicode_from_response(
    get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'))
a = open(r"nginx_logs.txt", "w+", encoding="utf-8")
a.write(response)
sp_ = []
a.seek(0)

with open ("nginx_logs.txt", "r", encoding="utf-8") as f:
    pro = [(line.split()[0], line.split()[5], line.split()[6]) for line in f]
    for i in pro:
        print(i)
