# Simple demo for AWS SAM application

[![Action Status](https://github.com/zhangran1/software_engineering_demo/workflows/aws-sam-demo/badge.svg)](https://github.com/zhangran1/software_engineering_demo/actions)

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders

- docs - Design docs.
- apps - Code for the application's Lambda function.
- scripts - Docker Scripts to initialize database and python scripts to insert database value
- tests/units - Unit tests for the application code. 
- tests/.api_test - API tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

This application is tested in Ubuntu 16.04 LTS. Due to python packages compatible issue, it might not work with other OS. 

## Project setup
Please kindly configure python virtual environment to test the project. 

## Local Test the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3.7 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)
* Docker-Compose [Install Docker Compost](https://docs.docker.com/compose/install/)
* AWS credentials configured

Remarks:
If you are using python virtual enviroment, please make sure the project started in python3.7 virtual environment.
If you are using any other virtual enviroment version, random bugs may occur.

```
python3.7 -m venv py37-venv
```

## Setup database
For local testing the database used is postgres and launch in docker container. For testing purpose, please update the 
following configuration in /scripts/docker_scripts/docker-compose.yml

    
    - POSTGRES_USER="Change-it"
    - POSTGRES_PASSWORD="Change-it"

For testing purpose, please kindly use 5432 as port number. If you change the port number, please 
change docker expose port mapping accordingly.

## Setup database for SAM application.
After configure the postgres database, please kindly update the  /apps/db_confi.py postgres database credential
shall match with the previous step docker database's credential. Please note about the end point address remarks, for  the ip  shall be 192.168.1.x
or any other ip address instead of localhost or 127.0.0.1

You may use any unique value eg uuid for database_lock_id. Please do not use "228b27e3-2a74-4849-9eba", this is hard code test database lock. 

```
endpoint = "Please update use your local ip and avoid use localhost or 127.0.0.1"
port = ""
db_user = ""
password = ""
database = ""
database_lock_id = ""
```

## Setup database for SAM application Automatically.
All bash command shall be executed at application's root directory.

Please kill any existing process
```
sh sh_kill_ports.sh
```

Start docker compose first before start the next script.
```
sh start_docker_first.sh
```

You may just execute local_start.sh to automatically perform `sam build`, database lock setup and test

```bash
sh local_start.sh
```

## Setup database for SAM application Manually.
Start database and initialize database schema and insert locks.

```bash
pip install -r apps/requirements.txt
docker-compose -f scripts/docker_scripts/docker-compose.yml up &
python scripts/init_db/init_db.py
```

## Use the SAM CLI to build and test locally

Kill any running ports for 3000 and 5432. If you are changing port configuration. Please update accordingly.
```bash
sudo kill -9 `sudo lsof -t -i:3000`
sudo kill -9 `sudo lsof -t -i:5432`
```

Install python dependencies and Build your application with the `sam build` command.

```bash
sam validate
sam build
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
sam local start-api &
```



## Unit tests

Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests.

```bash
pytest
```

## API test
Tests are defined in the `tests/.api` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests.

```bash
pytest tests/.api_test/
```

API entry points for start docker locally
USER STORY 1: Upload Users
```
http://127.0.0.1:3000/users/upload [POST]  
```

USER STORY 2: Employee Dashboard Feature
```
http://127.0.0.1:3000/users [GET]
```

USER STORY 3: CRUD Feature (Bonus)
```
http://127.0.0.1:3000/users/{id}/ [PATCH]
http://127.0.0.1:3000/users/{id}/ [GET]
http://127.0.0.1:3000/users/{id}/ [POST]
http://127.0.0.1:3000/users/{id}/ [DELETE]
```

## Known bug
1. Post to following url without pathparameter will incur error
```
http://127.0.0.1:3000/users/
```

2. Post to following url without query string will incur error
```
http://127.0.0.1:3000/users
```

3. Delete existing user no checking, if there user had been logically deleted user should not be deleted again.
For example if user `test-1234` exist in database, if two delete operation performed on this user is, both will return 
http 200. 

## Future Enhancement
1. Code refactor for folder structure
2. More test cases
