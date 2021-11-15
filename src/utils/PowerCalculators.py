import numpy as np


def calculate_rms(samples: list):
    buffer = np.array(samples)
    buffer = np.power(buffer, 2)
    mean_of_squares = np.average(buffer)
    rms = np.sqrt(mean_of_squares)
    return float(rms)


def calculate_voltage(samples: list):
    return float(np.array(samples).mean())


def calculate_power(voltage: float, current: float):
    return voltage * current
