from collections import defaultdict
from temperature_measurement import TemperatureMeasurement
from pprint import pprint

#def find_start_excusion_time(data):
#
#def find_stop_excursion_time(data):
#
#def calculate_total_duration(data):
#Find when the temperature goes out of range
#Find the first time the temperature is out of range (sensors send data at the same time, some sensors sense a different temperature
#Have to take into consideration the sensor
#Sensor A one time can sense when something goes out of range. Find the first time it senses out of range and then next time its in range
#find the next time its back in range
#calculate the distance of time between the two

#find the time and temps for each sensor (some sort of dictionary with each sensor)
#find the first instance out of range. Then for that sensor, find the next time it comes into range. Calculate time. For that data, know the type, and get the highest temp, or the lowest temp depending on type.

class TemperatureTracker:

    def create_temperature_measurements(self, data):
        for line in data:
            measurement_objects = self.__convert_to_measurement_objects(line['tmps'])

        return measurement_objects

    def find_temperatures_excursion_event(self, data):
        temperature_data = []
        for line in data:
          range_data = map(self.__find_sensor_temperatures, line['tmps'])
          temperature_data.append(range_data)

        return temperature_data

    def find_all_events(self, data, result):
      found_excursions = []

      if not data:
        #return found_excursions
        pprint('do we get here')
        return 0

      if data[0].is_excursion:
        pprint(data[0].temperature)
        found_excursions.append(data[0])
        found_excursions.append(self.find_all_events(data[1:], found_excursions))

      return found_excursions

      #for item in data:
      #  pprint(item.temperature)
      #  if item.is_excursion:
      #    start_position = data.index(item)
      #    found_excursions.append(item)
      #    next_incursion = self.find_all_events(data[start_position:])

    def __convert_to_measurement_objects(self, data):
        return [self.__convert(item) for item in data]

    def __convert(self, data):
        sensor_id = data['sId']
        time = data['time']
        temperature_type = self.__determine_temp_type(data['tmp'])
        temperature = data['tmp']
        event_type = self.__determine_if_excursion(temperature_type)

        temperature_measurement = TemperatureMeasurement(sensor_id, time, temperature_type, temperature, event_type)
        return temperature_measurement

    def __determine_temp_type(self, temperature):
        if temperature >= 8:
            return 'hot'
        elif temperature <= 2:
            return 'cold'
        else:
            return 'na'

    def __determine_if_excursion(self, temperature_type):
        return temperature_type != 'na'

    def __find_sensor_temperatures(self, data):
        groups = defaultdict(list)

        for obj in data:
                groups[obj['sId']].append(obj)

        new_list = groups.values()
        pprint(new_list)
#        counts = dict()
#        for i in data:
#              counts[i] = counts.get(i, 0) + 1
#

    def __find_out_of_range_temps(self, data):
        temperature = data['tmp']
        if (temperature >= 8) or (temperature <= 2):
          d = {}
          d["time"] = data['time']
          d["temperature"] = temperature
          return d
