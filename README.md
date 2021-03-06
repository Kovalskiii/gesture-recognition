# gesture-recognition
Prediction of gestures based on capturing of muscles contractions and ML

Based on PyoMyo library.

## plot-emg-data-mat.py
Capturing of RAW EMG data using myo armband and python matplotlib.
Captured data are plotted in Matplotlib .  8 graphs are created - every graph for 1 armband sensor.
<p align="center">
<img src="https://media.giphy.com/media/M4q78uavYRvMCujwwf/giphy.gif" alt="Left to Right Wrist movements."/>
</p>



Capturing filtred EMG data using myo armband and python matplotlib.
Captured data are plotted in Matplotlib .  8 graphs are created - every graph for 1 armband sensor.
(Bandpass filter + rectified) (mode 0x01)
<p align="center">
<img src="https://media.giphy.com/media/qjhIhmUNO2JbnqoSU5/giphy.gif" alt="Left to Right Wrist movements."/>
</p>


## plot-emg-data-arr.py
RAW EMG data (array of 8 values) 
<p align="left">
<img src="https://user-images.githubusercontent.com/49062638/140205893-b74ea059-c285-4f72-9635-e165c32f0d19.png"/>
</p>


Filtred EMG data(array of 8 values)(Bandpass filter + rectified) (mode 0x01)
<p align="left">
<img src="https://user-images.githubusercontent.com/49062638/140199268-85fbd995-0382-468f-b3e8-53aca5298c2e.png"/>
</p>


## emg-data-classifier.py
This script is dedicated to capture data from armband 
and learn (improve model) in real time.

It is using k-nearest neighbors algorithm.

Labbeled data are stored as array.

In order to delete all the data press E button on the keyboard.

Press numbers from 0 to 9 to label data.
<p align="left">
<img src="https://user-images.githubusercontent.com/49062638/140199707-048817b8-9bdd-4de5-bb9d-872aa89da0d0.png"/>
</p>

https://youtu.be/xZ1mQtPdz5I


## emg-data-classifier-anim2.py
This script is dedicated to capture data from armband, learn (improve model) in real time and show real-time hand animation.

(Start emg-data-classifier-anim.py, then in the project folder find folder HandAnim and run Hand.exe) (In hand animation was used Godot Engine)
Script is using k-nearest neighbors algorithm.

Labbeled data are stored as array.

In order to delete all the data press E button on the keyboard.

Press numbers from 0 to 9 to label data.

<p align="left">
<img src="https://user-images.githubusercontent.com/49062638/144508692-b1705fd8-9d9c-401e-8d75-0a00d9ef849e.png"/>
</p>


