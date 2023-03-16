from typing import Optional
import logging
import sqlite3
from utils.config import DB_NAME, TB_NAME


class city_states_data:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def get_coord(self, args: dict[str: str]) -> Optional[tuple]:
        city_name = args['city_name']
        state_id = args['state_id']
        logging.info(f"Reading database for coordinates and timezone for {city_name}, {state_id}")
        self.cursor.execute("SELECT lat, lon, timezone FROM '%(table)s' \
                             WHERE city = '%(city)s' AND state_id = '%(state_id)s' " \
                             % {'table': TB_NAME,'city': city_name, 'state_id': state_id})
        logging.info(f"Successfully retrieve from database for coordinates and timezone for {city_name}, {state_id}")
        rows = self.cursor.fetchall()
        self.connection.close()
        return rows[0] if len(rows) != 0 else None

    def get_states(self) -> Optional[list[tuple]]:
        logging.info("Reading database for list of states")
        self.cursor.execute("SELECT DISTINCT(state_id) FROM '%(table)s' \
                            ORDER BY state_id ASC"
                            % {'table': TB_NAME})
        logging.info("Successfully retrieve from database for list of states")
        rows = self.cursor.fetchall()[: -1]
        rows = [item for t in rows for item in t]
        self.connection.close()
        return {'stateIds' : rows}

if __name__ == '__main__':
    city_states_data().get_states()
