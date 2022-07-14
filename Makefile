clean:
	rm -rf react_cli.egg-info

setup:
	python3 -m pip install --editable .

lint:
	python3 -m pylint -v -f=colorized -r=y src/**/*
