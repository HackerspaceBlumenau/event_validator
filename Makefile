
flake:
	flake8 action.py test.py

test:
	python3 -m unittest discover

image:
	podman build -f Dockerfile .
all: flake test
