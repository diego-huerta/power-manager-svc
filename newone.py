import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn

# Data collection setup
FACTOR = 42.425519
RATE = 3300
SAMPLES = 1000

# test
# Create the I2C bus with a fast frequency
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0, ADS.P1)

# ADC Configuration
ads.mode = Mode.CONTINUOUS
ads.data_rate = RATE

data = [None]*SAMPLES

start = time.monotonic()

# Read the same channel over and over
for i in range(SAMPLES):
    data[i] = chan.voltage

print('antes' + '\t' + 'despues')
for sample in data:
    print(str(sample) + '\t' + str(sample * FACTOR))

#end = time.monotonic()
#total_time = end - start

#print("Time of capture: {}s".format(total_time))
#print("Sample rate requested={} actual={}".format(RATE, SAMPLES / total_time))
