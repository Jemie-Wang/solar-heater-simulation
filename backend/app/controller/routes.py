import logging
from flask import Blueprint, request
from app.service.effi_service import effic_service
from app.service.city_states_service import city_states_service
from app.controller.response_warper import warper_generator

warper = warper_generator()
city_states_service = city_states_service()
effic_service = effic_service()

states = Blueprint('states', __name__)

@states.route("/", methods=['GET'])
def returnStates():
    # Log message when /states route is called
    logging.info('Getting all states')
    
    # Get all the states from the service layer
    response = city_states_service.get_states()
    
    # Return the response with success message using the warper
    return warper.sucess_message(response)


coordinate = Blueprint('coordinate', __name__)

@coordinate.route("/coordinate", methods=['GET'])
def returnCoord():
    # Log message when /coordinate route is called
    logging.info('Getting coordinates for city')
    
    # Get the query parameters as a dictionary
    args = request.args.to_dict()
    
    # Get the coordinates and timezone from the service layer
    response = city_states_service.get_coord_and_timezone(args)
    
    # If response is None, return not found error message with 404 status code, else return the response with success message using the warper
    if(response == None):
        response = warper.not_found_message({"error": "City name incorrect or state id mismatch, please retry"})
    else:
        response = warper.sucess_message(response)
    
    return response


efficiency = Blueprint('efficiency', __name__)

@efficiency.route("/efficiency", methods=['GET'])
def returnEffi():
    # Log message when /efficiency route is called
    logging.info('Getting efficiency data')
    
    # Get the query parameters as a dictionary
    args = request.args.to_dict()
    
    # Get the efficiency data from the service layer
    response = effic_service.get_effic(args)
    
    # Return the response with success message using the warper
    return warper.sucess_message(response)
