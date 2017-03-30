import requests
from BeautifulSoup import BeautifulSoup

url = "http://www.kuet.ac.bd/index.php/welcome/transportation"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.findAll('table', attrs={'width':'880','border':'1','cellspacing':'0'})

datas = []
rowNo = 0
colNo = 0

for i in table:
	for row in i.findAll('tr'):
		for cell in row.findAll('td'):
			datas[rowNo].append(cell.text)
		rowNo = rowNo + 1

print (datas)

