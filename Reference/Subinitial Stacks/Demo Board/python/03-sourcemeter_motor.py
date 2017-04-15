# importing the Python-provided time library to access delays (time.sleep)
import time

# importing the Subinitial library to access the Stacks commands
import subinitial.stacks as stacks

# Connecting to the Stacks Core and Analog Deck
core = stacks.Core(host="192.168.1.49")
analogdeck = stacks.AnalogDeck(core_deck=core, bus_address=2)

# --------------APPLICATION CODE-------------- #

# Loop the Sourcemeter code infinitely
while True:
    # Ramp up motor speed/voltage from 0V to 10V every 1/2 second
    for set_voltage in range(0, 11):
        analogdeck.sourcemeter.set_sourcevoltage(volts=set_voltage)
        time.sleep(0.5)

    # Ramp down motor speed/voltage from 10V to 0V every 1/2 second
    for set_voltage in range(10, -1, -1):
        analogdeck.sourcemeter.set_sourcevoltage(volts=set_voltage)
        time.sleep(0.5)
