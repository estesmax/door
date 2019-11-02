image:
	docker build -t jchorl/door .

dev:
	docker run -it --rm \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-v $(PWD):$(PWD):ro \
		-w $(PWD) \
		docker/compose:1.24.1 \
		-f docker-compose-dev.yml up

build-image:
	docker build -t jchorl/door .

build-compose-image:
	cd ../compose
	docker build -t jchorl/compose .
	cd -

deploy: build-image build-compose-image
	docker run -d --rm \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-v $(PWD)/docker-compose.yml:$(PWD)/docker-compose.yml:ro \
		-w $(PWD) \
		--restart=always \
		docker/compose:1.24.1 \
		up
