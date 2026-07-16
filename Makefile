.PHONY: install test lint run build up down smoke

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest

lint:
	flake8 app tests

run:
	uvicorn app.main:app --reload

build:
	docker build -t tienda-agora-api:2.0.0 .

up:
	docker compose up --build -d

down:
	docker compose down

smoke:
	python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8000/health').read().decode())"
