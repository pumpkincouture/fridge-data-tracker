from pprint import pprint

#def find_start_excusion_time(data):
#
#def find_stop_excursion_time(data):
#
#def calculate_total_duration(data):
#Find when the temperature goes out of range
#Find the time the temperature is out of range
#Filter the results to find the distance of time between each out of range occurance (have to have chronological time order)
#Start time is the first instance of that range, end time is the measure of time distance between the next occurance of out of range
#Total duration is the time distance between ranges

class TemperatureTracker:

    def find_temperatures_excursion_event(self, data):
        temperature_data = []
        for line in data:
          range_data = map(self.__find_out_of_range_temps, line['tmps'])
          temperature_data.append(range_data)

        pprint(temperature_data)
        return temperature_data

    def __find_out_of_range_temps(self, data):
        temperature = data['tmp']
        if (temperature >= 8) or (temperature <= 2):
          d = {}
          d["time"] = data['time']
          d["temperature"] = temperature
          return d
