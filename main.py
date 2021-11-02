from pyomyo import Myo

#  _lucky duck_
#       __
#      /__\
#     >(' )
#       )/
#      /(
#     /  `----/
#     \  ~=- /
#   ~^~^~^~^~^~^~^

def main():
    m = Myo()
    m.connect()
    m.vibrate(2)

    def handle_emg(emg, movement):
        print(emg)

    m.add_emg_handler(handle_emg)

main()