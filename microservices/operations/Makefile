
docker_built: tested
	docker build -t nishedcob/operations-base .
	touch $@

tested: base_app.py Dockerfile requirements.txt test.sh
	./test.sh
	touch $@
