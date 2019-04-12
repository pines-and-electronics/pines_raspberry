raspistill -t 10000 -tl 2000 -o /home/pi/Documents/pines_raspberry/pines_raspberry_img/images/image%04d.jpg


source activate pines_conda


python /home/pi/Documents/pines_raspberry/pines_raspberry_img/gcp_vision_multi_img.py
