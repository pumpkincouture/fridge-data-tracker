from lib.temperature_tracker import TemperatureTracker
import json

def extract_file_data(files):
  with open(files) as data_file:
    for line in data_file:
      data = json.loads(line)
      temperature_tracker = TemperatureTracker()
      temperature_tracker.find_temperatures_excursion_event(data['data'])

extract_file_data('techtest_1.json')
