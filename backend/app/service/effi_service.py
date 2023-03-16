import math
import datetime
import pandas as pd
from app.data.solar_data import solar_data

class effic_service:

    def __init__(self):
        self.solar_data = solar_data()
        
    def _calc_effi(self, row):
        elevation = math.radians(row['apparent_elevation'])  # apparent elevation angle in radians
        if elevation <= 0:
            return 0
        azimuth = math.radians(row['azimuth'] - 180)  # azimuth angle in radians

        solar_effi = (math.sin(self.panel_angle) * math.cos(azimuth) * math.cos(elevation) + math.cos(self.panel_angle) * math.sin(elevation)) \
                      * (1 - self.absorb_rate) * self.pipe_effi

        if solar_effi < 0:
            solar_effi = 0

        return solar_effi


    def get_effic(self, args: dict[str: str]) -> dict:
        self.panel_angle= math.radians(int(args.get('panel_angle')))
        self.absorb_rate= int(args.get('absorb_rate')) / 100
        self.pipe_effi= int(args.get('pipe_efficiency')) / 100
        start_date= args.get('start')
        start= datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end= start + datetime.timedelta(hours=23)
        lat= args.get('lat')
        lon= args.get('lon')
        tz = args.get('timezone')
        solar_query= {'start': start, 'end': end, 'lat': lat, 'lon': lon, 'tz': tz}
        solar_info_dict = self.solar_data.get_solar_data(solar_query)
        solar_info = pd.DataFrame.from_dict(solar_info_dict).transpose()
        solar_info['effi'] = solar_info.apply(self._calc_effi, axis= 1)
        return solar_info['effi'].to_dict()


if __name__ == "__main__":
    effic_service.get_effic({"lat": "43.4872000000", "lon" : "-112.036399999999999", "start" : "2035-01-07", "end" : "2035-01-07"})