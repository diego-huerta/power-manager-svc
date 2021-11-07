import board
import busio
import numpy as np
import adafruit_ads1x15.ads1115 as ADS
import tempfile
import itertools
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn


class CurrentMonitor:
    FREQUENCY = 1000000
    RATE = 3300
    SAMPLE_SIZE = 1000
    FACTOR = 42.425519
    CHANNEL = None

    def __init__(self, frequency, rate, sample_size, factor):
        self.RATE = rate
        self.SAMPLE_SIZE = sample_size
        self.FACTOR = factor
        i2c = busio.I2C(board.SCL, board.SDA, frequency=self.FREQUENCY)
        ads = ADS.ADS1115(i2c)
        ads.mode = Mode.CONTINUOUS
        ads.data_rate = self.RATE
        self.CHANNEL = AnalogIn(ads, ADS.P0, ADS.P1)

    def take_samples(self):
        buffer = [None] * self.SAMPLE_SIZE
        for i in range(self.SAMPLE_SIZE):
            buffer[i] = self.CHANNEL.voltage
        return buffer

    def calculate_rms(self, samples):
        buffer = np.array(samples)
        buffer = np.power(buffer, 2)
        mean_of_squares = np.average(buffer)
        rms = np.sqrt(mean_of_squares)
        return float(rms)

    def save_to_tmpfile(self, samples):
        tempfile._get_candidate_names = lambda: itertools.repeat('current_samples')
        with tempfile.NamedTemporaryFile(dir='/tmp') as f:
            f.writelines(samples)

