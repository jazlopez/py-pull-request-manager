install:
	pip3 install -r requirements.txt

test:
	python3 -m unittest -v tests/*.py

coverage:
	coverage3 run tests/*.py && coverage3 html -d output_html/

