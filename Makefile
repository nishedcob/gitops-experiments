
komposed: docker-compose.yaml
	kompose convert
	mkdir -vp ops/k8s
	mv -v sum-deployment.yaml ops/k8s/
	touch $@
