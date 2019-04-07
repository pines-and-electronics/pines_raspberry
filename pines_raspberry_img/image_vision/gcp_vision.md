---
title: GCP Vision
---

####  [Project Page](https://dujm.github.io/Iot_EdgeComputing/index)&nbsp;  | &nbsp;   [AWS IoT Setup](https://dujm.github.io/Iot_EdgeComputing/aws_iot)&nbsp;  | &nbsp;   [GCP IoT Setup](https://dujm.github.io/Iot_EdgeComputing/gcp_iot)



### 1. Set up Google Cloud Platform (GCP)
 * Go to [Create service account key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.262041677.-1312817518.1554382349&project=quiet-mechanic-236610&folder&organizationId)
  * Select project on top 'pines1'
  * Service account, my account 
  * JSON
 * Provide authentication credentials to your application code 
 * [Enable] billing(https://console.developers.google.com/billing/enable?project=650311275390) 

 ```
 export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/gcp/pines1-6e82e765805d.json"
 ``` 
 
### 2. Install GCP SDK
[Installing with apt-get for Debian and Ubuntu](https://cloud.google.com/sdk/docs/downloads-apt-get)  

 ```
cd pines_raspberry 

export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update && sudo apt-get install google-cloud-sdk 
 ```


### 3. Setup the client library on RPI
### Setting Up a Python Development Environment
[Doc](https://cloud.google.com/python/setup)

 ```
sudo apt update
sudo apt install python python-dev python3 python3-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
#sudo pip install --upgrade virtualenv
# Successfully installed virtualenv-16.4.3

# Install google api 
[Doc](https://cloud.google.com/vision/docs/libraries#client-libraries-install-python)
cd Iot_EdgeComputing/env/bin
virtualenv --python python3 env

source env/bin/activate
sudo env/bin/pip install google-cloud-storage
sudo env/bin/pip install google-cloud-vision
sudo env/bin/pip install google-api-python-client


# If you want to stop using the virtualenv and go back to your global Python, you can deactivate it:
#deactivate 
 ```
 
### 4. Setup GCloud SDK
 ```
gcloud init
 ```
 
### 5. Authorizing Cloud SDK tools
 ```
gloud auth login
gcloud auth application-default login
[Authorizing a service account?](https://cloud.google.com/sdk/docs/authorizing)

gcloud auth list
 ```

### 6. Test using a local image (tree)
 * cd pines_raspberry/image_vision 
 * Write a python file /home/pi/Iot_EdgeComputing/gcp_vision.pines.py

 * gcp_vision.pines.py  
 
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

### 7. [Add members](https://console.cloud.google.com/cloud-resource-manager?_ga=2.63823599.-1312817518.1554382349)


### 8. To do 
Warinings 
/home/pi/Documents/pines_raspberry/env/bin/env/lib/python3.5/site-packages/google/auth/_default.py:66: UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK. We recommend that most server applications use service accounts instead. If your application continues to use end user credentials from Cloud SDK, you might receive a "quota exceeded" or "API not enabled" error. For more information about service accounts, see https://cloud.google.com/docs/authentication/
  warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)
Labels: