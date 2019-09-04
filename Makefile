#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004
#
#  Copyright (C) 2019 JAZIEL LOPEZ SOFTWARE ENGINEER jlopez.mx
#
#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.
#
#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#   0. You just DO WHAT THE FUCK YOU WANT TO.

install:
	pip3 install --ignore-installed -r requirements.txt 2> /dev/null

test:
	python3 -m unittest -v tests/*.py

coverage:
	rm -rf output_html/
	coverage3 run --include client.py,tests/*.py  -m unittest tests/*.py
	coverage3 html -d output_html/