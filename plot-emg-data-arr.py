# #  _lucky duck_
# #       __
# #      /__\
# #     >(' )
# #       )/
# #      /(
# #     /  `----/
# #     \  ~=- /
# #   ~^~^~^~^~^~^~^

'''
This script is dedicated to plot in the terminal live EMG data (array on 8 values).
To exit - press Ctrl + C in the terminal.
'''

import multiprocessing
from pyomyo import Myo, emg_mode

# ------------ Myo Setup ---------------
q = multiprocessing.Queue()

def worker(q):
	m = Myo(mode=emg_mode.PREPROCESSED)
	m.connect()
	
	def add_to_queue(emg, movement):
		q.put(emg)

	m.add_emg_handler(add_to_queue)
	
	def print_battery(bat):
		print("Battery level:", bat)

	m.add_battery_handler(print_battery)

	# Orange logo and bar LEDs
	m.set_leds([128, 0, 0], [128, 0, 0])
	# Vibrate on success connection
	m.vibrate(1)
	
	"""worker function"""
	while True:
		m.run()
	print("Worker Stopped")

# -------- Main Program Loop -----------
if __name__ == "__main__":
	p = multiprocessing.Process(target=worker, args=(q,))
	p.start()

	try:
		while True:
			while not(q.empty()):
				emg = list(q.get())
				print(emg)

	except KeyboardInterrupt:
		print("Quitting")
		quit()