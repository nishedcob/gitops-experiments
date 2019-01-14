
CONFIG_FILE=../config.yaml

komposed: docker-compose.yaml Makefile
	kompose convert
	mkdir -vp k8s
	mv -v sum-deployment.yaml k8s/
	touch $@

docker-compose.yaml: docker-compose.yaml.j2 config.yaml
	python3 template_renderer.py --config $(CONFIG_FILE) --template $< --output $@

clean_all:
	rm -v komposed docker-compose.yaml || exit 0
