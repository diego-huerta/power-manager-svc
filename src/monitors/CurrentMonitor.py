import time

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn
from src.utils.RMSCalculator import take_samples as ts
from src.utils.RMSCalculator import calculate_rms as crms
from src.utils.FilesUtils import save_to_tmpfile


class CurrentMonitor:
    FREQUENCY = 1000000
    RATE = 3300
    SAMPLE_SIZE = 20
    FACTOR = 42.425519
    C_CHANNEL = None
    V_CHANNEL = None

    def __init__(self, frequency, rate, sample_size, factor):
        self.FREQUENCY = frequency
        self.RATE = rate
        self.SAMPLE_SIZE = sample_size
        self.FACTOR = factor
        i2c = busio.I2C(board.SCL, board.SDA, frequency=self.FREQUENCY)
        ads = ADS.ADS1115(i2c)
        ads.mode = Mode.CONTINUOUS
        ads.data_rate = self.RATE
        self.C_CHANNEL = AnalogIn(ads, ADS.P0, ADS.P1)
        self.V_CHANNEL = AnalogIn(ads, ADS.P1, ADS.P2)
        self.start_recording()

    def start_recording(self):
        while True:
            samples = ts(
                current_input_channel=self.C_CHANNEL,
                voltage_input_channel=self.V_CHANNEL,
                sample_size=self.SAMPLE_SIZE
            )
            rms = crms(samples[0])
            save_to_tmpfile('raw_current', samples[0])
            save_to_tmpfile('raw_voltage', samples[1])
            save_to_tmpfile('rms', rms)
            time.sleep(0.5)
