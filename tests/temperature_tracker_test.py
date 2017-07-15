from temperature_tracker import TemperatureTracker
import unittest
import json
import os.path
import ast
from pprint import pprint
temps = os.path.join(os.path.dirname(__file__), './fixtures/temperatures.json')
times_and_temps = os.path.join(os.path.dirname(__file__), './fixtures/temperatures_and_times.txt')

class TemperatureTrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.temperature_tracker = TemperatureTracker()
        self.temperatures = ast.literal_eval(open(temps).read())
        self.temps_and_time = ast.literal_eval(open(times_and_temps).read())

    def test_find_out_of_range_temperatures(self):
        original_data = [{"dId":"358072045332183","tmps":[{"sId":"A","time":1461732679,"typ":0,"tmp":8.9},{"sId":"B","time":1461732679,"typ":2,"tmp":8.3},{"sId":"C","time":1461732679,"typ":0,"tmp":23.2},{"sId":"D","time":1461732679,"typ":0,"tmp":23.1},{"sId":"E","time":1461732679,"typ":0,"tmp":23.5} ]}]
        expected_data = [[{"time": 1461732679, "temperature": 8.9},{"time":1461732679,"temperature":8.3},{"time":1461732679,"temperature":23.2},{"time":1461732679,"temperature":23.1},{"time":1461732679,"temperature":23.5}]]

        call = self.temperature_tracker.find_temperatures_excursion_event(self.temperatures)

        self.assertEqual(call, self.temps_and_time)

    def test_find_time_duration_of_excursion_event(self):
        input_data = [[{"time": 1461732679, "temperature": 8.9},{"time":1461732679,"temperature":8.3},{"time":1461732679,"temperature":23.2},{"time":1461732679,"temperature":23.1},{"time":1461732679,"temperature":23.5},{"time":1461732679,"temperature":23.5}]]

        call = self.temperature_tracker.find_duration_of_event(input_data)



if __name__ == '__main__':
  unittest.main()
