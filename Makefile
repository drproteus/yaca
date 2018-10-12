build:
	python setup.py py2app
	mv dist/main.app dist/yaca.app

.PHONEY: clean, package

clean:
	rm -rf build/ dist/

package:
	cd dist && zip yaca.zip yaca.app
