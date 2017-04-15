# importing the Python-provided time library to access delays (time.sleep)
import time

# importing the Subinitial library to access the Stacks commands
import subinitial.stacks as stacks

# Connecting to the Stacks Core and Analog Deck
core = stacks.Core(host="192.168.1.49")
analogdeck = stacks.AnalogDeck(core_deck=core, bus_address=2)

# --------------APPLICATION CODE-------------- #

# Set the Wavegen to apply a DC voltage, which is connected to DMM channel 0 on the Demo Board through SW2
analogdeck.wavegen.set_control(analogdeck.wavegen.MODE_DC)

print('NOTE: Adjust WAVEGEN switch (SW2) to connect/disconnect Wavegen to DMM.')

# Loop the DMM code infinitely
while True:
    # Ramp up Wavegen voltage, measure and print value each step
    for set_voltage in range(0, 6):
        analogdeck.wavegen.set_dc(volts=set_voltage)

        measured_voltage = analogdeck.dmm.measure_channel(channel=0)
        print("Wavegen set voltage: {0:.3f} V.   DMM measured voltage: {1:.6f}".format(set_voltage, measured_voltage))

        time.sleep(0.5)

    # Ramp down Wavegen voltage, measure and print value each step
    for set_voltage in range(5, -1, -1):
        analogdeck.wavegen.set_dc(volts=set_voltage)

        measured_voltage = analogdeck.dmm.measure_channel(channel=0)
        print("Wavegen set voltage: {0:.3f} V.   DMM measured voltage: {1:.6f}".format(set_voltage, measured_voltage))

        time.sleep(0.5)
