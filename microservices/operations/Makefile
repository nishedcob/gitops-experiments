
CONFIG_FILE=../../config.yaml

all_apps: Makefile base_app sum_app
	touch $@

base_app: Makefile docker_built
	touch $@

sum_app: Makefile base_app sum/**
	touch sum/parent_built
	cd sum ; make
	touch $@

docker_built: tested
	date --utc '+%Y%m%d%H%M%S' > $@
	docker build -t "nishedcob/operations-base:$$(cat $@)" . || rm -v $@
	sed "s/\(docker_ops_base_curr_version:\s*\)'\?\"\?.*'\?\"\?/\1'"$$(cat $@)"'/" -i $(CONFIG_FILE) || rm -v $@
	docker push "nishedcob/operations-base:$$(cat $@)" || rm -v $@
	touch $@

tested: base_app.py Dockerfile requirements.txt test.sh
	./test.sh
	touch $@

clean_all:
	rm -v all_apps base_app sum_app docker_built tested || exit 0
	cd sum ; make clean_all
