
all_apps: Makefile all_operations_apps
	touch $@

all_operations_apps: Makefile operations/**
	cd operations ; make all_apps
	touch $@

base_operation_app: Makefile operations/*
	cd operations ; make base_app
	touch $@

sum_operation_app: Makefile operations/* operations/sum/**
	cd operations ; make sum_app
	touch $@
