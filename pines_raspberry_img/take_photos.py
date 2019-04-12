raspistill -t 10000 -tl 2000 -o image%04d.jpg

#This will produce a capture every 2 seconds over a total period of 10s, named image1.jpg, image0002.jpg...image0015.jpg.


raspistill -t 10000 -tl 2000 -o /home/pi/Documents/pines_raspberry/pines_raspberry_img/images/image%04d.jpg
