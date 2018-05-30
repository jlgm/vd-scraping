# vd-scraping
# https://github.com/jlgm/vd-scraping

# Author: jlgm

setup:
	@pip install bs4 --user
	@pip install anytree --user
	@pip install prettytable --user
	@pip install --user

start:
	@python src/main.py

test:
	@python -m unittest discover src/