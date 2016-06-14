.PHONY: help
.DEFAULT_GOAL := help

BAKE_OPTIONS=--no-input

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

bake:
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

watch: bake
	watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.repo_name}}/

replay: BAKE_OPTIONS=--replay
replay: watch
	;
