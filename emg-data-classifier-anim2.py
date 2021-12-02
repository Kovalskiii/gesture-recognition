import pygame
from pygame.locals import *
import numpy as np
from sklearn import neighbors

from classifierLib import emg_mode
from classifierLib import Classifier, MyoClassifier, EMGHandler
import matplotlib.pyplot as plt
from matplotlib import animation
import bone
import multiprocessing
import godot

SUBSAMPLE = 3 
K = 15   #15
RESET_SCALE = True

class KNN_Classifier(Classifier):
	'''SKLearn k-NN implimentation'''

	def __init__(self):
		Classifier.__init__(self)

	def train(self, X, Y):
		self.X = X
		self.Y = Y
		self.model = None
		if self.X.shape[0] >= K * SUBSAMPLE:
			self.model = neighbors.KNeighborsClassifier(n_neighbors=K, algorithm='kd_tree')
			self.model.fit(self.X[::SUBSAMPLE], self.Y[::SUBSAMPLE])

	def classify(self, emg):
		x = np.array(emg).reshape(1,-1)
		if self.X.shape[0] < K * SUBSAMPLE: 
			return 0

		pred = self.model.predict(x)
		return int(pred[0])


	# def nearest(self, d):
	# 	dists = ((self.X - d)**2).sum(1)
	# 	ind = dists.argmin()
	# 	return self.Y[ind]

	# def classify(self, d):
	# 	if self.X.shape[0] < K * SUBSAMPLE: return 0
	# 	return self.nearest(d)

def text(scr, font, txt, pos, clr=(255,255,255)):
	scr.blit(font.render(txt, True, clr), pos)

fig = plt.figure("Finger plots from Myo")
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')

q = multiprocessing.Queue(10000)

def make_animate(q):
	def animate(i):
		fingers = [0,0,0,0,0]
		emgs = [0,0,0,0,0,0,0,0]
		while not(q.empty()):
			fingers = list(q.get())
		# Plot
		ax.clear()
		ax.set_xlabel('X [mm]')
		ax.set_ylabel('Y [mm]')
		ax.set_zlabel('Z [mm]')
		if (RESET_SCALE == True):
			ax.set_xlim3d([-0.05, 0.1])
			ax.set_ylim3d([-0.1, 0.1])
			ax.set_zlim3d([0, 0.2])

		points = bone.lerp_fingers(fingers, bone.right_open_pose, bone.right_fist_pose)

		# Plot the Points
		bone.plot_steam_hand(points, "Lerped Pose", ax)
	return animate

def do_plot(q):
	anim = animation.FuncAnimation(fig, make_animate(q), blit=False, interval=1)
	plt.show(block=True)
if __name__ == '__main__':
	pygame.init()
	w, h = 800, 320
	scr = pygame.display.set_mode((w, h))
	font = pygame.font.Font(None, 30)

	p = multiprocessing.Process(target=do_plot, args=(q,), daemon=True)
	p.start()
	godot.start()

	m = MyoClassifier(KNN_Classifier(), mode=emg_mode.PREPROCESSED)
	hnd = EMGHandler(m)
	m.add_emg_handler(hnd)
	m.connect()

	m.add_raw_pose_handler(print)

	try:
		while True:
			m.run()

			r = m.history_cnt.most_common(1)[0][0]

			# Handle keypresses
			for ev in pygame.event.get():
				if ev.type == QUIT or (ev.type == KEYDOWN and ev.unicode == 'q'):
					raise KeyboardInterrupt()
				elif ev.type == KEYDOWN:
					if K_0 <= ev.key <= K_9:
						hnd.recording = ev.key - K_0
					elif K_KP0 <= ev.key <= K_KP9:
						hnd.recording = ev.key - K_KP0
					elif ev.unicode == 'r':
						hnd.cl.read_data()
					elif ev.unicode == 'e':
						print("Erased local data, by Pressing E button")
						m.cls.delete_data()
				elif ev.type == KEYUP:
					if K_0 <= ev.key <= K_9 or K_KP0 <= ev.key <= K_KP9:
						hnd.recording = -1

			# Plotting
			scr.fill((0, 0, 0), (0, 0, w, h))
			#print(m.history_cnt)
			total = sum(m.history_cnt.values(), 0.0)
			fingers = [ m.history_cnt[i] / total for i in range(1, 6)]
			#print(f"{fingers=}")
			godot.update_pose(fingers)
			q.put(fingers)

			for i in range(10):
				x = 0
				y = 0 + 30 * i

				clr = (0,200,0) if i == r else (255,255,255)

				txt = font.render('%5d' % (m.cls.Y == i).sum(), True, (255,255,255))
				scr.blit(txt, (x + 20, y))

				txt = font.render('%d' % i, True, clr)
				scr.blit(txt, (x + 110, y))

				# Plot the history of predicitons
				scr.fill((0,0,0), (x+130, y + txt.get_height() / 2 - 10, len(m.history) * 20, 20))
				scr.fill(clr, (x+130, y + txt.get_height() / 2 - 10, m.history_cnt[i] * 20, 20))

			pygame.display.flip()

	except KeyboardInterrupt:
		pass
	finally:
		m.disconnect()
		print()
		pygame.quit()