from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        to get components
        '''
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary=dict(query_string_list)
        # definitions=
        
        if 'country' in dictionary:
            word = dictionary['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + word)
            data = r.json()
            capital=data[0]['capital']
            country=data[0]['name']['common']
                
            message=f'The capital of {country} is {capital}.'

        elif 'capital' in dictionary:
            word = dictionary['capital']
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + word)
            data = r.json()
            capital=data[0]['capital']
            country=data[0]['name']['common']
                
            message=f'{capital} is the capital of {country}'

        else :
            message="please provide me with a word"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        self.wfile.write(message.encode())
        return