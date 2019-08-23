install:
	pip3 install -r requirements.txt

test:
	python3 -m unittest -v tests/*.py

coverage:
	rm -rf output_html/
	coverage3 run --include client.py,tests/*.py  -m unittest tests/*.py
	coverage3 html -d output_html/