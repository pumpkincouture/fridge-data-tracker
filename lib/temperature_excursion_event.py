class TemperatureExcursionEvent:
    def __init__(self, start_excursion_time, stop_excursion_time, total_excursion_duration, excursion_type):
        self.start_excursion_time = start_excursion_time
        self.stop_excursion_time = stop_excursion_time
        self.total_excursion_duration = total_excursion_duration
        self.excursion_type = excursion_type

