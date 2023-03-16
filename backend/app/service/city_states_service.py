import datetime
import pytz
from app.data.city_states_data import city_states_data


class city_states_service:

    # def __init__(self):
    #     self.city_states_data = city_states_data()
        
    def get_coord_and_timezone(self, args: dict[str: str]):
        cityinfo = city_states_data().get_coord(args)
        if cityinfo == None:
            return None
        time_diff = self._convert_timezone(cityinfo[-1])
        return {'lat': cityinfo[0], 'lon': cityinfo[1], 'tz': time_diff}

    def get_states(self):
        return city_states_data().get_states()

        
    def _convert_timezone(self, iana_tz: str) -> int:


        # Set the time zone you want to compute the difference with UTC
        tz = pytz.timezone(iana_tz)

        utc_time = pytz.utc.localize(datetime.datetime.utcnow())

        # Convert UTC time to the desired time zone
        local_time = utc_time.astimezone(tz)

        # Compute the time difference in hours
        time_diff = (local_time.utcoffset().total_seconds() / 3600)

        return time_diff

if __name__ == '__main__':
    # Notice that the city name and state id is case sensitive
    city_states_service().get_coord_and_timezone('New York', 'NY')
