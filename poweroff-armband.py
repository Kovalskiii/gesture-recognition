import time
from pyomyo import Myo, emg_mode

'''
Script is dedicated to power off the Myo armband.
If armband is motionless for some time it goes into sleep mode and
can be woken by shaking.
Truly turn the armband OFF it is needed to esend a power off command as (m.power_off()).
To turn armband ON we need to connect it to the power.
'''

# Make a Myo object
m = Myo(mode=emg_mode.RAW)
# Connect to armband
m.connect()
print("Turning the Myo armband off.")
print("To turn armband ON - connect it to the power.")
print("Press Ctrl + Break.")
m.vibrate(2)
# Wait until it vibrates before turning it off
time.sleep(2)
# Turn it off
m.power_off()
quit()