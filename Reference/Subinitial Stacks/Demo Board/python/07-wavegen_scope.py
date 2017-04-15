# importing the Subinitial library to access the Stacks commands
import subinitial.stacks as stacks

# Connecting to the Stacks Core and Analog Deck
core = stacks.Core(host="192.168.1.49")
analogdeck = stacks.AnalogDeck(core_deck=core, bus_address=2)

# --------------APPLICATION CODE-------------- #

# Load a waveform to the Wavegen memory. A waveform is an arbitrary list of voltage samples at a specified sample-rate
analogdeck.wavegen.update_waveform(samplerate_hz=30e3, samples=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] * 30)

# Set the Wavegen to apply a continuously-looping waveform instead of a DC voltage
analogdeck.wavegen.set_control(analogdeck.wavegen.MODE_WAVEFREERUN)

print('NOTE: Use oscilloscope to probe TP5 to see the output waveform. Set scope to 100us/div and 2V/div.')
