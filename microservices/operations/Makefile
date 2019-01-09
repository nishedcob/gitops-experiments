
all_apps: Makefile base_app sum_app
	touch $@

base_app: Makefile docker_built
	touch $@

sum_app: Makefile base_app sum/**
	touch sum/parent_built
	cd sum ; make
	touch $@

docker_built: tested
	docker build -t nishedcob/operations-base .
	touch $@

tested: base_app.py Dockerfile requirements.txt test.sh
	./test.sh
	touch $@
