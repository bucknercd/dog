NGINX_IMAGE=ng_doggy
NGINX_CONTAINER=ng_container_doggy
WEBAPP_IMAGE=web-app_doggy
WEBAPP_CONTAINER=web-app_container_doggy
WEBAPP_CONTAINER_2=web-app_container_2_doggy
WEBAPP_CONTAINER_3=web-app_container_3_doggy
API_IMAGE=api_doggy
API_CONTAINER=api_container_doggy
MONGO_IMAGE=mongo_image_doggy
MONGO_CONTAINER=mongo_container_doggy

help:
	echo "\n*** Makefile Commands ***\nbuild-nginx\\nrun-nginx\nshell-nginx\nkill-nginx\n\n\
build-web-app\nrun-web-app\ntest-web-app\nrun-web-app-2\nrun-web-app-3\nshell-web-app\nkill-web-app\nkill-web-app-2\nkill-web-app-3\n\n"

build-nginx:
	docker build -t $(NGINX_IMAGE) -f nginx.dockerfile .
run-nginx:
	docker run -p 443:443 -d --rm --name $(NGINX_CONTAINER) $(NGINX_IMAGE)
shell-nginx:
	docker exec -it $(NGINX_CONTAINER) bash
test-nginx:
	docker run -p 443:443 --rm --name $(NGINX_CONTAINER) $(NGINX_IMAGE)
kill-nginx:
	docker rm $(NGINX_CONTAINER) -f


build-web-app:
	docker build -t $(WEBAPP_IMAGE) -f web-app.dockerfile .
run-web-app:
	docker run -p 9000:80 -d --rm --name $(WEBAPP_CONTAINER) $(WEBAPP_IMAGE)
run-web-app-2:
	docker run -p 9001:80 -d --rm --name $(WEBAPP_CONTAINER_2) $(WEBAPP_IMAGE)
run-web-app-3:
	docker run -p 9002:80 -d --rm --name $(WEBAPP_CONTAINER_3) $(WEBAPP_IMAGE)
shell-web-app:
	docker exec -it $(WEBAPP_CONTAINER) bash
test-web-app:
	docker run -it -p 9000:80 --rm --name $(WEBAPP_CONTAINER) $(WEBAPP_IMAGE) /bin/bash
kill-web-app:
	docker rm $(WEBAPP_CONTAINER) -f
kill-web-app-2:
	docker rm $(WEBAPP_CONTAINER_2) -f
kill-web-app-3:
	docker rm $(WEBAPP_CONTAINER_3) -f


build-api:
	echo 'build-api'


build-mongo:
	docker build -t $(MONGO_IMAGE) -f mongodb.dockerfile .
test-mongo:
	docker run -it --rm --name $(MONGO_CONTAINER) $(MONGO_IMAGE) /bin/bash
run-mongo:
	docker run --rm --name $(MONGO_CONTAINER) $(MONGO_IMAGE)


clean:
	docker system prune
	make kill-nginx
	make kill-web-app
	make kill-web-app-2
	make kill-web-app-3
doggy:
	make build-nginx
	make build-web-app
	make run-nginx
	make run-web-app
	make run-web-app-2
	make run-web-app-3
