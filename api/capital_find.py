from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    url=self.path
    urlComponent=parse.urlsplit(url)
    query=parse.parse_qsl(urlComponent.query)
    mydic=dict(query)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    if 'capital' in mydic:
        capitalValue=mydic.get('capital')
        Api=f'https://restcountries.com/v3.1/capital/{capitalValue}'
        ApiReq=requests.get(Api)
        JsonVar=ApiReq.json()
        for i in JsonVar:
            value=i["name"]['common']
            message=f'{capitalValue} is the capital of {value}'
    if 'country' in mydic:
        countryValue=mydic.get('country')
        ApiLink=f'https://restcountries.com/v3.1/name/{countryValue}'
        ApiReqL=requests.get(ApiLink)
        JsonVar2=ApiReqL.json()
        for i in JsonVar2:
            value2=i["capital"][0]
            message=f'The capital of {countryValue} is {value2}'
    self.wfile.write(message.encode())
    return







