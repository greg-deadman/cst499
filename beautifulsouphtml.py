#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

#use requests to pull html from espn site
html_doc = requests.get('https://www.espn.com/nba/schedule')
#create soup object to get document content and set mode of bs4 to parsing
soup = BeautifulSoup(html_doc.content, 'html.parser')
#find all html classes that have team name, using 'a' because we need to find a tags in document
teams = soup.find_all("a", class_ = "team-name")
#create a dict
nbadict = {}
#for loop allows for cleanup, count, and more narrow parsing
for team in teams:
    #create new soup object to parse for just teams
    teamsoup = BeautifulSoup(str(team), 'html.parser')
    #find span tags from parsed teamsoup
    teamsoup.find_all("span")
    #eliminating 'span' tags and receiving just names
    name = teamsoup.get_text()
    #adding one to game count
    if name in nbadict:
        nbadict[name] += 1
    #adding new entry if team name not seen before
    else:
        nbadict[name] = 1

#print teams and game counts
print(nbadict)

#html_doc.text will give you the string