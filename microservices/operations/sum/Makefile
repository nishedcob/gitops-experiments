
docker_built: tested
	docker build -t nishedcob/operations-sum .
	touch $@

tested: parent_built Dockerfile test.sh doctest.sh
	./doctest.sh
	./test.sh
	touch $@

parent_built: ../base_app.py ../Dockerfile ../requirements.txt ../test.sh
	cd .. ; make
	touch $@
