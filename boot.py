
#Taken from here:
#https://www.robmiles.com/journal/2025/1/14/taking-control-of-circuitpython-disabling-and-restoring-usb-mass-storage

import storage
import usb_cdc

# Disable USB mass storage
storage.disable_usb_drive()

# Keep USB REPL enabled to allow deploying files via REPL tools
usb_cdc.enable(console=True, data=True)

# Remount the filesystem so CircuitPython code can write to it
storage.remount("/", readonly=False)

