#!/bin/bash
pip install -r apps/requirements.txt
python scripts/init_db/init_db.py
sam validate
sam build
sam local start-api &
pytest
pytest tests/.api_test/
