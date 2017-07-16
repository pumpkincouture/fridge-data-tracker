class TemperatureMeasurement:
    def __init__(self, sensor_id, time, temperature_type, temperature, is_excursion):
        self.sensor_id = sensor_id
        self.time = time
        self.temperature_type = temperature_type
        self.temperature = temperature
        self.is_excursion = is_excursion
