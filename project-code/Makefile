DESTDIR=server

all: start
	@echo "DONE"

docker-all: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build -t sp19-222-101/spam
	@echo "imgage DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -i -t -p 8080:8080 sp19-222-101/spam /bin/bash

service:
	@echo "creating the service..."
	pip install --upgrade pip
	pip install -r requirements.txt

start:
	@echo "starting the service"
	pip install --upgrade pip
	pip install -r requirements.txt
	python server.py

docker-stop:
	@echo "stopping the service"
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image"
	docker rmi -f sp19-222-101/spam
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)