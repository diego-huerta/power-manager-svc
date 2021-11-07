import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn

# Data collection setup
FACTOR = 42.425519
RATE = 3300
SAMPLES = 40

# test
# Create the I2C bus with a fast frequency
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0, ADS.P1)

# ADC Configuration
ads.mode = Mode.CONTINUOUS
ads.data_rate = RATE

data = [None] * SAMPLES

# Read the same channel over and over
def take_samples(buffer, number_of_samples):
    for i in range(number_of_samples):
        buffer[i] = chan.voltage

take_samples()

print('antes' + '\t' + 'despues')
for sample in data:
    print(str(sample) + '\t' + str(sample * FACTOR))

# print("Time of capture: {}s".format(total_time))
# print("Sample rate requested={} actual={}".format(RATE, SAMPLES / total_time))



