import pandas as pd

def export(data):
	df = pd.DataFrame(data)
	df.to_csv("Report_Card")



def total(a,b):
	return a + b


