# importing the Python-provided time library to access delays (time.sleep)
import time

# importing the Subinitial library to access the Stacks commands
import subinitial.stacks as stacks

# Connecting to the Stacks Core and Analog Deck
core = stacks.Core(host="192.168.1.49")
analogdeck = stacks.AnalogDeck(core_deck=core, bus_address=2)

# --------------APPLICATION CODE-------------- #

# Configure the DIGITAL I/O (DIO's) 0-3 as outputs
analogdeck.dio.set_config(dio0_3_innotout=False)

# Loop the blinking code infinitely
while True:
    # Turning on all output DIO's
    analogdeck.dio.set(0, 1, 2, 3)

    # Delay for 1 second
    time.sleep(1)

    # Turn off all output DIO's
    analogdeck.dio.clear(0, 1, 2, 3)

    # Delay for 1 second
    time.sleep(1)
