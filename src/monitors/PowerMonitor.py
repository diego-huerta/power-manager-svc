import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
import src.utils.PowerCalculators as Calculator
import src.utils.SampleUtils as Sampler
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn
from src.utils.FilesUtils import create_tmpfile
from src.utils.FilesUtils import save_to_tmpfile


class PowerMonitor:
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

    def start_recording(self):
        with create_tmpfile('raw_current') as raw_current_file, \
                create_tmpfile('raw_voltage') as raw_voltage_file,\
                create_tmpfile('rms') as rms_file, \
                create_tmpfile('power') as power_file:
            while True:
                samples = Sampler.take_mixed_samples(
                    current_input_channel=self.C_CHANNEL,
                    voltage_input_channel=self.V_CHANNEL,
                    sample_size=self.SAMPLE_SIZE
                )
                rms = Calculator.calculate_rms(samples[0])
                mean_voltage = Calculator.calculate_voltage(samples[1])
                power = Calculator.calculate_power(mean_voltage, rms)
                save_to_tmpfile(raw_current_file.name, samples[0])
                save_to_tmpfile(raw_voltage_file.name, samples[1])
                save_to_tmpfile(rms_file.name, rms)
                save_to_tmpfile(power_file.name, power)
                time.sleep(0.5)
