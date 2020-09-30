#!/bin/bash
pip install -r apps/requirements.txt
docker-compose -f scripts/docker_scripts/docker-compose.yml up &
python scripts/init_db/init_db.py
sam validate
sam build
sam local start-api &
pytest
pytest tests/.api_test/
