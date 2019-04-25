DESTDIR=server

all: start
	@echo "DONE"

docker-all: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build --no-cache --pull -t sp19-222-101/spam:latest .
	@echo "imgage DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -t -p 8080:8080 sp19-222-101/spam 

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
	docker ps -a
	docker ps -a > dockerContainers.txt
	python remove_container.py

docker-clean: docker-stop docker-remove
	@echo "DONE"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)
