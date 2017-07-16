from lib.temperature_tracker import TemperatureTracker
from lib.temperature_excursion_event import TemperatureExcursionEvent
import json
from pprint import pprint
from itertools import chain
from itertools import groupby
from collections import defaultdict
import numpy as np
import pandas as pd

def extract_file_data(files):
  temperature_data = []
  with open(files) as data_file:
    for line in data_file:
      data = json.loads(line)
      temperature_tracker = TemperatureTracker()
      objects = temperature_tracker.create_temperature_measurements(data['data'])
      temperature_data.append(objects)

  return temperature_data

def find_excursion(data):
  found_excursions = []
  found_incursions = []
  for item in data:
      if item.is_excursion:
        start_position = data.index(item)
        next_incursion = find_next_incursion(data[start_position:])
        #pprint(next_incursion)

#this will find the next time temperature is in range
#item to find will be item.temperature_type == 'na'
def find_next_incursion(data):
  first = 0
  last = len(data)-1
  found = False
  items = []

  while( first<=last and not found):
    mid = (first + last)//2
    pprint(data[mid])
    if not data[mid].is_excursion:
      pprint(data[mid].temperature)
      pprint(data[mid].event_type)
      found = True
      items.append(data[mid])
    else:
      if data[mid].temperature_type.is_excursion:
        last = mid - 1
      else:
        first = mid + 1
  return items

data = extract_file_data('sample_file2.json')
flattened_data = list(chain.from_iterable(data))

groups = defaultdict(list)

for obj in flattened_data:
  groups[obj.sensor_id].append(obj)

new_list = groups.values()

my_array = np.array(new_list)

for sensor_data in new_list:
    sorted_list = sorted(sensor_data, key=lambda item: item.time)
    #filtered_by_time_range = filter(lambda item: 1461196800 <= item.time <= 1461888000, sorted_list)
    #each internal array

    [ pprint(item.time) for item in sorted_list ]
    #pprint(sorted_list[-1].sensor_id)
    #pprint(sorted_list[0].temperature)
    #pprint(sorted_list[0].time)
    #pprint(sorted_list[0].is_excursion)
    #find_excursion(filtered_by_time_range)

