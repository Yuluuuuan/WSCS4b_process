requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f process
	brane remove -f process
	brane build container.yml
	brane push process