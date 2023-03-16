import json
with open('utils/config.json', 'r') as f:
    config = json.load(f)
HOST = config['host']
PORT_NUM = config['port_number']
ORIGN= config['frontend_origin']
DEBUG_MODE = config['debug_mode']
SOLAR_API = config['solar_api']
DB_NAME = config['database_name']
TB_NAME = config['table_name']
