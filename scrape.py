from bs4 import BeautifulSoup
import requests
import sys

year = 2020 
if len(sys.argv) > 1: year = sys.argv[1]
url = "https://www.pro-football-reference.com/years/{}/passing.htm".format(str(year))
r = requests.get(url)
if r.status_code != 200:
    print("ERROR: {} is an invalid year".format(str(year)))
    exit(1)
soup = BeautifulSoup(r.text, 'html.parser')

# Get table
table = soup.find(class_="table_container")
# Get body
tbody = table.find('tbody')
tr_body = tbody.find_all('tr')
qbs = []

for trb in tr_body:
    for td in trb.find_all('td'):
        # Get case value
        val = (td.get_text())
        # Get data-stat value
        stat = td.get('data-stat')
        #print(stat)
        if stat == 'player':
            player = val
        if stat == 'pass_int':
            inter = int(val)
        if stat == 'pass_td':
            touchdown = int(val)
        if stat == 'pass_att':
            att = int(val)
        if stat == 'pass_yds':
            yards = int(val)
        if stat == 'g':
            games = int(val)
    if games ==0 or att < 150:
        continue
    rating = float((inter * 20 + touchdown * 20 + yards) / att) * float(.25 * att/games)
    qbs.append((player, rating))
qbs = sorted(qbs, key=lambda tup: tup[1], reverse=True)
for qb in qbs:
    print(qb)

