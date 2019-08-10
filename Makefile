dev:
	uvicorn main:app --reload

test:
	PYTHONPATH=${PYTHONPATH}:${PWD} pipenv run pytest tests/
