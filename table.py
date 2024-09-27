import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_national_capitals'

tables = pd.read_html(url)

df = tables[1]

print(df.head())