PROJECT_NAME ?= tg-encyclopedia
VERSION = $(shell python3 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= temaxuck
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

clean: 
	rm -fr *.egg-info dist

lint:
	venv/bin/pylama

sdist: clean
	python3 setup.py sdist

docker_build: sdist
	docker build --target=api -t $(PROJECT_NAME):$(VERSION) .

docker_run: docker_build
	docker run --name=$(PROJECT_NAME)-bot -d --publish 8080:8080 $(PROJECT_NAME):$(VERSION)

docker_upload: docker_build
	docker tag $(PROJECT_NAME):$(VERSION) $(REGISTRY_IMAGE):$(VERSION)
	docker tag $(PROJECT_NAME):$(VERSION) $(REGISTRY_IMAGE):latest
	docker push $(REGISTRY_IMAGE):$(VERSION)
	docker push $(REGISTRY_IMAGE):latest