
komposed: docker-compose.yaml Makefile
	kompose convert
	mkdir -vp k8s
	mv -v sum-deployment.yaml k8s/
	touch $@
