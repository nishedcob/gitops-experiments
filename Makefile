
everything: build_apps ops_config
	touch $@

build_apps: Makefile microservices/**
	cd microservices ; make all_apps
	touch $@

build_operations: Makefile microservices/* microservices/operations/*
	cd microservices ; make all_operations_apps
	touch $@

build_operations_sum: Makefile microservices/* microservices/operations/* microservices/operations/sum/**
	cd microservices ; make sum_operation_app
	touch $@

ops_config: ops/komposed
	cd ops ; make komposed
	touch $@
