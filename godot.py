from flask import Flask
from threading import Thread
from math import sin
from time import time

pose = [0, 0, 0, 0, 0]

def run():
    app = Flask(__name__)
    @app.route('/pose')
    def get_pose():
        p = pose
        return {
            "thumb": p[0],
            "index": p[1],
            "middle": p[2],
            "ring": p[3],
            "pinky": p[4],
        }
    app.run("0.0.0.0", 8123, debug=True, use_reloader=False)

def update_pose(p):
    global pose
    pose = p

def start():
    t = Thread(target=run, daemon=True)
    t.start()


if __name__ == "__main__":
    start()
    while True:
        update_pose([sin(time()) for _ in range(5)])