from temperature_tracker import TemperatureTracker
from temperature_measurement import TemperatureMeasurement
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

    #def test_find_out_of_range_temperatures(self):
        #call = self.temperature_tracker.find_temperatures_excursion_event(self.temperatures)

        #self.assertEqual(call, self.temps_and_time)

    def test_find_start_and_end_excursion_event(self):
        call = self.temperature_tracker.find_all_events(self.__mock_temperature_measurements(), [])

        events = self.__mock_excursion_events

        self.assertEqual(call, events)

    def __mock_temperature_measurements(self):
      temperature_measurement1 = TemperatureMeasurement('A', 1461723079, 'hot', 9, True)
      temperature_measurement2 = TemperatureMeasurement('A', 1461723679, 'hot', 10, True)
      temperature_measurement3 = TemperatureMeasurement('A', 1461724279, 'hot', 13, True)
      temperature_measurement4 = TemperatureMeasurement('A', 1461724879, 'na', 7.5, False)

      measurements = [ temperature_measurement1, temperature_measurement2, temperature_measurement3, temperature_measurement4 ]
      return measurements

    def __mock_excursion_events(self):
      excursion_1 = TemperatureExcursionEvent(1461723079, 1461724879, 1800, 'hot', 13)
      excursions = [ excursion_1 ]
      return excursions


if __name__ == '__main__':
  unittest.main()
