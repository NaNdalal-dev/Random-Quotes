from pandas import read_csv

df = read_csv('random.csv',sep=';')

def Quote(num):
	try:
		return df.iloc[num]
	except:
		return None
