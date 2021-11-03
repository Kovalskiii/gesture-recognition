# gesture-recognition
Prediction of gestures based by capturing of muscles contractions and ML

Based on PyoMyo library.

### plot-emg-data-mat.py
<iframe src="https://giphy.com/embed/M4q78uavYRvMCujwwf" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/M4q78uavYRvMCujwwf">via GIPHY</a></p>
Capturing of RAW EMG data using myo armband and python matplotlib.
Captured data are plotted in Matplotlib .  8 graphs are created - every graph for 1 armband sensor.

<div style="width:100%;height:0;padding-bottom:83%;position:relative;"><iframe src="https://giphy.com/embed/M4q78uavYRvMCujwwf" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/M4q78uavYRvMCujwwf">via GIPHY</a></p>
Capturing filtred EMG data using myo armband and python matplotlib.
Captured data are plotted in Matplotlib .  8 graphs are created - every graph for 1 armband sensor.
(Bandpass filter + rectified) (mode 0x01)

### plot-emg-data-arr.py
RAW EMG data (array on 8 values) 
<p align="left">
<img src="https://user-images.githubusercontent.com/49062638/140205893-b74ea059-c285-4f72-9635-e165c32f0d19.png"/>
</p>


Filtred EMG data(array on 8 values)(Bandpass filter + rectified) (mode 0x01)
<p align="left">
<img src="https://user-images.githubusercontent.com/49062638/140199268-85fbd995-0382-468f-b3e8-53aca5298c2e.png"/>
</p>

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


