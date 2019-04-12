---
title: Set Up a muleai environment on rpi
---


### 1. create muleai environment using yml file
 * Modify yml file 
 ```
name: muleai
channels:
  - rpi
  - defaults
  - conda-forge
dependencies:
 - pip:
  - pandas==0.23.3
  - tensorflow==1.8.0
prefix: /home/pi/miniconda3/envs/muleai


 ```

conda env create -f requirements_offline_training.yml 


### Errors:
ResolvePackageNotFound: 


 Could not find a version that satisfies the requirement html5lib==0.9999999=py36_0
 
 No matching distribution found for grpcio==1.12.1=py36hdbcaa40_0
 
### Removed from 2.yml 
 * Remove everything from conda dependencies, add to pip
     - _tflow_180_select==3.0=eigen
     - html5lib==0.9999999=py36_0
      - grpcio==1.12.1=py36hdbcaa40_0
