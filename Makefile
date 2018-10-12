build:
	python setup.py py2app
	mv dist/main.app dist/yaca.app

.PHONEY: clean

clean:
	rm -rf build/ dist/
