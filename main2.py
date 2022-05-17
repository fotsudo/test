#!/usr/bin/env python
import time
from adc import ADC

adc = ADC

while True:
# Read channel 0(Slot A0) voltage
    print(adc.read_voltage(0))
    time.sleep(1)