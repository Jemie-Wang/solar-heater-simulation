from flask import Flask
from utils.config import HOST, PORT_NUM, DEBUG_MODE
from app.controller.routes import states, coordinate, efficiency

# create the app object
app = Flask(__name__)

# register the routes
app.register_blueprint(states)
app.register_blueprint(coordinate)
app.register_blueprint(efficiency)

# start the server
if __name__ == '__main__':
    app.run(host=HOST, port=PORT_NUM, debug=DEBUG_MODE)
