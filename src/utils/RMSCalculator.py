import numpy as np
from adafruit_ads1x15.analog_in import AnalogIn


def take_samples(current_input_channel: AnalogIn, voltage_input_channel: AnalogIn,  sample_size: int) -> tuple:
    current_buffer = [None] * sample_size
    voltage_buffer = [None] * sample_size
    for i in range(sample_size):
        current_buffer[i] = current_input_channel.voltage
        voltage_buffer[i] = voltage_input_channel.voltage

    # TODO: Replace this tuple with a custom class
    return current_buffer, voltage_buffer


def calculate_rms(samples: list):
    buffer = np.array(samples)
    buffer = np.power(buffer, 2)
    mean_of_squares = np.average(buffer)
    rms = np.sqrt(mean_of_squares)
    return float(rms)
