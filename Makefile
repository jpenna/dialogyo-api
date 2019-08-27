dev:
	uvicorn main:app --reload --port 23400

test:
	PYTHONPATH=${PYTHONPATH}:${PWD} pipenv run pytest tests/
