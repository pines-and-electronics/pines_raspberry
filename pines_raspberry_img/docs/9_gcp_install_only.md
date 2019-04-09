---
title: 0 GCP Setup
---

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

export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update && sudo apt-get install google-cloud-sdk 
 ```
 
### 3. Setup GCloud SDK
 ```
gcloud init
 ```
 
### 4. Authorizing Cloud SDK tools
 ```
gloud auth login
gcloud auth application-default login
[Authorizing a service account?](https://cloud.google.com/sdk/docs/authorizing)

gcloud auth list
 ```

### 5. [Add members](https://console.cloud.google.com/cloud-resource-manager?_ga=2.63823599.-1312817518.1554382349)


### 6. Errors
 * ModuleNotFoundError: No module named 'google'
 pip install --upgrade google-api-python-client
 
 * ModuleNotFoundError: No module named 'google.cloud'

