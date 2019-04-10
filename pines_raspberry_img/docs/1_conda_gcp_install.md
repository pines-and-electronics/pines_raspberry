---
title: Set Up a Python Environment using conda
---


### 1. Install miniconda
[Doc](https://www.hackster.io/lbtinglb/install-opencv-through-miniconda-in-second-on-rasberry-pi-3-4eec27)
[Raspberry Pi 3 Python3](https://medium.com/@lin7lic/%E5%9C%A8raspberry-pi-3-%E5%AE%89%E8%A3%9Dpython-3-opencv-34c9740d78e4)  

```
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
sudo md5sum Miniconda3-latest-Linux-armv7l.sh
sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh
# Change dir to /home/pi/miniconda3

# Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /root/.bashrc ? [yes|no]: no 
sudo vim /home/pi/.bashrc

# Add the following line to the end of the file
export PATH=/home/pi/miniconda3/bin:$PATH
source ~/.bashrc

# Remove miniconda3
# sudo -s
# rm -r /home/pi/miniconda3
```

### 2. Install python 3.6  

```  
conda config --add channels rpi
conda install python=3.6
```  

### 3. Create enviorment using conda  

``` 
conda create --name pines_conda python=3.6 -y

# Check enviorment list 
conda env list
# or 
conda info --envs
'''
# conda environments:

base                  *  /home/pi/miniconda3
pines_conda              /home/pi/miniconda3/envs/pines_conda

'''

# Remove enviorment 
# conda env remove --name pines_conda 
```  

### 4. Activate enviorment for Linux (Mac)
```
source activate pines_conda

'''
(pines_conda) pi@raspberrypi:~/Documents/pines_raspberry/conda $ 
'''
# Library list
conda list
```

### 5. Install packages
### 5.1 Install opencv in enviorment
```
conda install -y -c conda-forge opencv

# Check
python
>>>import cv2
>>>cv2.__version__
>>>'3.3.0'
``` 
### 5.2 Install Tensorflow in enviorment

``` 
pip install tensorflow
``` 

### 6. GCP setup 

### 6.1 Set up Google Cloud Platform (GCP)
 * Go to [Create service account key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.262041677.-1312817518.1554382349&project=quiet-mechanic-236610&folder&organizationId)
  * Select project on top 'pines1'
  * Service account, my account 
  * JSON
 * Provide authentication credentials to your application code 
 * [Enable billing](https://console.developers.google.com/billing/enable?project=650311275390) 

```
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/gcp/pines1-6e82e765805d.json"
``` 
 
### 6.2 Install Google SDK in enviorment
```
pip install google-cloud-storage
pip install google-cloud-vision
pip install google-api-python-client

```
### 6.3 Setup GCloud SDK
 ```
gcloud init
 ```
 
### 6.4. Authorizing Cloud SDK tools
```
gloud auth login
gcloud auth application-default login
[Authorizing a service account?](https://cloud.google.com/sdk/docs/authorizing)

gcloud auth list
```

### 7. Test using a local image (tree)
 * cd pines_raspberry/pines_raspberry_img/image_vision 
 * Write a python file gcp_vision.pines.py
 * python gcp_vision.pines.py  
 
```
Labels:
Tree
shortleaf black spruce
Yellow fir
Columbian spruce
lodgepole pine
balsam fir
oregon pine
Tropical and subtropical coniferous forests
red pine
White pine
```
 
 
### Not working 
```
conda install -c conda-forge google-cloud-sdk 
conda install -y -c goosgle-api-python-client
```

### Reference
[Getting started with Python environments](https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307)

[Why you need Python environments and how to manage them with Conda](https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c)
