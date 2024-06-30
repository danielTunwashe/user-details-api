from flask_restx import Namespace,Resource
from flask import request, jsonify
import requests




userdetails_namespace = Namespace('userdetails', description=" A namespace for user details")



@userdetails_namespace.route('/api/hello')
class UserDetails(Resource):
    def get(self):

        """
            Return User details such as (IP address, Location and temperature)

        """
        visitor_name = request.args.get('vistor_name', 'Guest')
        client_ip = request.remote_addr


        #Geolocation API 
        geo_response = requests.get(f"http://ip-api.com/json/{client_ip}").json()
        location = geo_response.get('city','Unknown')


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