# gesture-recognition
Prediction of gestures based by capturing of muscles contractions and ML

Based on PyoMyo library.

### plot-emg-data-mat.py
<iframe src="https://giphy.com/embed/M4q78uavYRvMCujwwf" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/M4q78uavYRvMCujwwf">via GIPHY</a></p>
Capturing of RAW EMG data using myo armband and python matplotlib.
Captured data are plotted in Matplotlib .  8 graphs are created - every graph for 1 armband sensor.

<iframe src="https://giphy.com/embed/M4q78uavYRvMCujwwf" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/M4q78uavYRvMCujwwf">via GIPHY</a></p>
Capturing filtred EMG data using myo armband and python matplotlib.
Captured data are plotted in Matplotlib .  8 graphs are created - every graph for 1 armband sensor.
(Bandpass filter + rectified) (mode 0x01)

### plot-emg-data-arr.py
<p align="center">
<img src="https://user-images.githubusercontent.com/49062638/140205893-b74ea059-c285-4f72-9635-e165c32f0d19.png"/>
</p>
RAW EMG data (array on 8 values)

<p align="center">
<img src="https://user-images.githubusercontent.com/49062638/140199268-85fbd995-0382-468f-b3e8-53aca5298c2e.png"/>
</p>
Filtred EMG data(array on 8 values) (Bandpass filter + rectified) (mode 0x01)

### emg-data-classifier.py
<p align="center">
<img src="https://user-images.githubusercontent.com/49062638/140199707-048817b8-9bdd-4de5-bb9d-872aa89da0d0.png"/>
</p>
This script is dedicated to capture data from armband 
and learn (improve model) in real time.
It is using k-nearest neighbors algorithm.
Labbeled data are stored as array.
In order to delete all the data press E button on the keyboard.
Press numbers from 0 to 9 to label data.


