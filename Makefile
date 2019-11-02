image:
	docker build -t jchorl/door .

dev:
	docker run -it --rm \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-v $(PWD):$(PWD):ro \
		-w $(PWD) \
		docker/compose:1.24.1 \
		-f docker-compose-dev.yml up
