from src.monitors.PowerMonitor import PowerMonitor

monitor1 = PowerMonitor(frequency=1000000, rate=3300, sample_size=100, factor=42.425519)
monitor1.start_recording()
