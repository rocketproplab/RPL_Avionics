# importing the Subinitial library to access the Stacks commands
import subinitial.stacks as stacks

# Connecting to the Stacks Core and Analog Deck
core = stacks.Core(host="192.168.1.49")
analogdeck = stacks.AnalogDeck(core_deck=core, bus_address=2)

# --------------APPLICATION CODE-------------- #

# Configure the DIO's 0-3 as output and DIO's 4-7 as inputs
analogdeck.dio.set_config(dio0_3_innotout=False, dio4_7_innotout=True)
print('NOTE: Adjust the DIGITAL INPUT switch (SW1) to cause the input of DIO 5 to be high or low.')

# Prepare a storage variable
in_state_previous = None

# Loop the input code infinitely
while True:
    # Read the input
    in_state = analogdeck.dio.get_pin_status(pin=5)

    # If input has changed, notify user in the console and have the LED for DIO 3 follow the input
    if in_state != in_state_previous:
        print("Input state changed. New state is:", in_state)
        in_state_previous = in_state
        analogdeck.dio.cmd_pin(pin=3, cmd=in_state)  # make DIO 3 output follow state from DIO 5 input
