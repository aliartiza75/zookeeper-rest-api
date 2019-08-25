# Zookeeper REST API
This repository contains endpoint to perform operation on the Apache Zookeeper.

## Endpoints
Its under development!

## Setup 

Install the packages defined below for this project:

- python3+  
- pip3 # python package manager

##### Install the project specific pakages:

Follow the steps given below to install the project specific packages

To use virtual enviornment for this project follow the steps given below, this is an `optional` step:

* To create virtual environment
  ```sh
  $ virtualenv zk-env
  ```
* To activate virtual environment
  ```
  $ source zk-env/bin/activate
  ```
* To deactivate the virtual environemnt
  ```sh
  $ deactivate
  ```

```sh
$ cd ~/zookeeper-rest-api
$ pip3 install -r requirements.txt # install all packages defined in requirenments.txt file
$ pip3 freeze # to validate packeges have been installed 
```

## To start server

To start the server use the command given below:

```
$ flask run --host=$FLASK_HOST_IP --port=$((FLASK_HOST_PORT))
```

* Starting Zookeeper REST API:
  ```bash
  $ sudo docker run -it -e FLASK_ENV=development -e FLASK_HOST_IP=<0.0.0.0> -e FLASK_HOST_PORT=<5000>  -e ZOOKEEPER_IP=<zookeeper-ip> -e ZOOKEEPER_PORT=<zookeeper-port> -p 5000:5000  -d zookeeper-rest-api
  ```


* Starting Zookeeper REST API using UWsgi

uwsgi --wsgi-file app.py --callable app --http :5000



Refrences

* Riptutorials for configurations
