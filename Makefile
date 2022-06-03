requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f process 1.0.0
	brane remove -f process
	brane build container.yml
	brane push process
