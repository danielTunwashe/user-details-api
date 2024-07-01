from flask_restx import Namespace,Resource
from flask import request, jsonify
import requests




userdetails_namespace = Namespace('/', description=" A namespace for user details")



@userdetails_namespace.route('/api/hello')
class UserDetails(Resource):
    def get(self):

        """
            Return User details such as (IP address, Location and temperature)

        """
        visitor_name = request.args.get('visitor_name', 'Guest')
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

         # Use a test IP address if running locally
        if client_ip == '127.0.0.1':
            client_ip = '8.8.8.8'  # Example IP for testing

        # Use ipinfo.io for geolocation
        ipinfo_response = requests.get(f'https://ipinfo.io/{client_ip}/json').json()
        location = ipinfo_response.get('city', 'Unknown')


        #Weather api
        api_key = '86de27e47736cdbcf1a5d0a0523ef78d'
        weather_response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        ).json()
        temperature = weather_response['main']['temp']

        # Creating the response
        response = {
            "client_ip": client_ip,
            "location": location,
            "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
        }

        return jsonify(response)