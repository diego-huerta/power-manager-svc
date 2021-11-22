import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
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
    C_FACTOR = 42.425519
    V_FACTOR = 1
    C_CHANNEL = None
    V_CHANNEL = None

    def __init__(self, frequency, rate, sample_size, current_factor=42.425519, voltage_factor=42.425519):
        self.FREQUENCY = frequency
        self.RATE = rate
        self.SAMPLE_SIZE = sample_size
        self.C_FACTOR = current_factor
        self.V_FACTOR = voltage_factor
        i2c = busio.I2C(board.SCL, board.SDA, frequency=self.FREQUENCY)
        ads = ADS.ADS1015(i2c)
        ads.mode = Mode.CONTINUOUS
        ads.data_rate = self.RATE
        self.C_CHANNEL = AnalogIn(ads, ADS.P0, ADS.P1)
        self.V_CHANNEL = AnalogIn(ads, ADS.P2, ADS.P3)

    def start_recording(self):
        with create_tmpfile('raw_current') as raw_current_file, \
                create_tmpfile('raw_voltage') as raw_voltage_file,\
                create_tmpfile('rms') as rms_file, \
                create_tmpfile('power') as power_file:
            while True:
                c_samples = Sampler.take_single_samples(
                    channel=self.V_CHANNEL,
                    sample_size=self.SAMPLE_SIZE,
                    factor=self.V_FACTOR
                )
                v_samples = Sampler.take_single_samples(
                    channel=self.V_CHANNEL,
                    sample_size=self.SAMPLE_SIZE,
                    factor=self.V_FACTOR
                )
                rms = Calculator.calculate_rms(c_samples)
                mean_voltage = Calculator.calculate_voltage(v_samples)
                power = Calculator.calculate_power(mean_voltage, rms)
                save_to_tmpfile(raw_current_file, c_samples[0])
                save_to_tmpfile(raw_voltage_file, v_samples[1])
                save_to_tmpfile(rms_file, rms)
                save_to_tmpfile(power_file, power)
                time.sleep(0.5)
