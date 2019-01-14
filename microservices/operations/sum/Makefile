
CONFIG_FILE=../../../config.yaml

docker_built: tested Dockerfile
	date --utc '+%Y%m%d%H%M%S' > $@
	docker build -t "nishedcob/operations-sum:$$(cat $@)" . || rm -v $@
	sed "s/\(docker_ops_sum_curr_version:\s*\)'\?\"\?.*'\?\"\?/\1'"$$(cat $@)"'/" -i $(CONFIG_FILE) || rm -v $@
	docker push "nishedcob/operations-sum:$$(cat $@)" || rm -v $@
	touch $@

Dockerfile: Dockerfile.j2
	python3 template_renderer.py --config $(CONFIG_FILE) --template $< --output $@

tested: parent_built test.sh doctest.sh app.py
	./doctest.sh
	./test.sh
	touch $@

parent_built: ../base_app.py ../Dockerfile ../requirements.txt ../test.sh
	cd .. ; make base_app
	touch $@

clean_all:
	rm -v parent_built docker_built tested Dockerfile || exit 0
