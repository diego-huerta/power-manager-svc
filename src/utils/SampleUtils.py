from adafruit_ads1x15.analog_in import AnalogIn


def take_mixed_samples(current_input_channel: AnalogIn, voltage_input_channel: AnalogIn, sample_size: int) -> tuple:
    current_factor = 42.425519
    current_buffer = [None] * sample_size
    voltage_buffer = [None] * sample_size
    for i in range(sample_size):
        current_buffer[i] = current_input_channel.voltage * current_factor
        voltage_buffer[i] = voltage_input_channel.voltage  # TODO: Add voltage factor

    # TODO: Replace this tuple with a custom class
    return current_buffer, voltage_buffer
