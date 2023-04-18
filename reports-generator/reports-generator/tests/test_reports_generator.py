from reports_generator import __version__
from reports_generator import total


def test_version():
	assert __version__ == '0.0.1'



def test_total():
	results = total(1,10)
	assert results == 11