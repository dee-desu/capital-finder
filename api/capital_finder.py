from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        1. serverless function handle with a GET http request with a given country name that responds with a string 
        2. and handle with a GET http request with a given capital that responds with a string 
        3. and handle with a GET http request with a given capital and country name  that responds with a string 
        """
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary=dict(query_string_list)
        
        if 'country' in dictionary:
            country=dictionary['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()
                
            capital = str(data[0]['capital'][0])
            message = f'the capital of {country} is {capital}.' 

        elif 'capital' in dictionary:
            capital=dictionary['capital']
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + capital)
            data = r.json()
            country=str(data[0]['name']['common'])
            message=f'{capital} is the capital of {country}.'
        else :
            message="please provide a country name or its capital name"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        self.wfile.write(message.encode())
        return
