from flask import jsonify
from utils.config import ORIGN

class warper_generator:
    def not_found_message(self, error):
        # create a JSON response with the given error message
        response = jsonify(error)
        # add an Access-Control-Allow-Origin header to the response with the origin specified in the config
        response.headers.add('Access-Control-Allow-Origin', ORIGN) 
        return response, 404
    
    def sucess_message(self, message: dict[str, str]):
        # create a JSON response with the given success message
        response = jsonify(message)
        # add an Access-Control-Allow-Origin header to the response with the origin specified in the config
        response.headers.add('Access-Control-Allow-Origin', ORIGN) 
        return response, 200
