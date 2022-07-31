import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://tourism.gov.in/parliament-questions-loksabha"

data = requests.get(url).text
# print(data)

soup = bs(data,'html.parser')
# print(soup)

tables = soup.find_all('table')

table = soup.find('table', class_='views-table views-view-table cols-7')
# print(table)

df = pd.DataFrame(columns=['Sr.No.', 'Subject','Q.No','Q.Type', 'Date', 'Member','Downloads'])
# print(df)

for row in table.tbody.find_all('tr'):    
    columns = row.find_all('td')

    if (columns != []):
        srno = columns[0].text.strip()
        subject = columns[1].text.strip()
        qno = columns[2].text.strip()
        qtype = columns[3].text.strip()
        date = columns[4].text.strip()
        member = columns[5].text.strip()
        downloads = columns[6].text.strip()

        df = df.append({'Sr.No.':srno,'Subject':subject,'Q.No':qno,'Q.Type':qtype,'Date':date,'Member':member,'Downloads':downloads},ignore_index=True)

# print(df)

df.to_csv("scrapdata.csv")

read = pd.read_csv("scrapdata.csv",index_col="Sr.No.")
print(read)

  