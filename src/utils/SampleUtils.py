from adafruit_ads1x15.analog_in import AnalogIn


"""
This is depreacated. Do not use. It doesn't work correctly
"""
def take_mixed_samples(
        current_input_channel: AnalogIn,
        voltage_input_channel: AnalogIn,
        sample_size: int,
        current_factor: float,
        voltage_factor: float
) -> tuple:
    current_buffer = [None] * sample_size
    voltage_buffer = [None] * sample_size
    for i in range(sample_size):
        current_buffer[i] = current_input_channel.voltage * current_factor
        voltage_buffer[i] = voltage_input_channel.voltage * voltage_factor

    # TODO: Replace this tuple with a custom class
    return current_buffer, voltage_buffer


def take_single_samples(
        channel: AnalogIn,
        sample_size: int,
        factor: float,
        voltage_factor: float
) -> tuple:
    buffer = [None] * sample_size
    for i in range(sample_size):
        buffer[i] = channel.voltage * factor

    return buffer
