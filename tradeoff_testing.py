import requests
import re
from bs4 import BeautifulSoup
from lxml import html

page = requests.get('https://www.google.com/finance')
text_page = page.text

""" DOW JONES REGEX """
print('\n', 'Dow Jones Regex')
print('-------------------------------')
#search allows us to find the expressions we are looking for in the text; x and y only require one matching group to find a good expression, z took three to get the correct spot
x = re.search('class="[a-zA-Z|\d]{3,6}">([a-zA-Z|\s]{3,9})<\/div>', text_page)
y = re.search('aria-label="([a-zA-Z]{2,4})\s(by)\s(\S{3,7})"><div', text_page)
z = re.search('P2Luy (Ebnabc|Ez2Ioe)">([+-]?)([0-9]*.?[0-9]{1,})</span>(</div>){4}.{1,70}Dow Jones', text_page)

#concatenate the print to get the first task, print groups for each search; need to use group(2) for access to the correct number due to increase in number of matching groups
print('The ' + x.group(1) + ' is ' + y.group(1) + ' ' + y.group(2) + ' ' + y.group(3) + ' or ' + z.group(2) + z.group(3) + ' points' + '.')

""" DOW JONES BEAUTIFUL SOUP """
print('\n', 'Dow Jones Beautiful Soup')
print('-------------------------------')
#create instance of bs4
soup = BeautifulSoup(text_page, 'html.parser')
#print some of the sentence and find the literal string dow jones, end= to not create a new line for next print
print('The', end= " ")
#create variable to store all matches
tag = soup.find_all("div", "pKBk1e")
#output just the text from the match
print(tag[0].get_text(), end=" ")
#create variable to store all matches
tags = soup.find_all("div", "JwB6zf V7hZne")
#output just the text from the match
print('is', tags[0].get_text(), 'or', end=" ")
#create variable to store all matches
tags1 = soup.find_all("span", "P2Luy Ez2Ioe")
#output just the text from the match
print(tags1[0].get_text(), 'points.')


""" DOW JONES XPATH - not finished """
print('\n', 'Dow Jones XPath')
print('-------------------------------')

""" AUTHOR RETRIEVAL REGEX """
print('\n', 'Author Retrieval Regex')
print('-------------------------------')
#retrieve site and convert to string
page1 = requests.get('https://agilemanifesto.org/authors.html')
text_page1 = page1.text
#counter
i = 0
#list of authors
authors = re.findall('<b>([a-zA-Z|\s|.]{3,})<\/b>', text_page1)
#while i is less than the length of author list, print authors
while i < len(authors):
    #use the tuple to print the 1st item or the 0th part of the index
    print(authors[i])
    #increment
    i += 1

""" AUTHOR RETRIEVAL BEAUTIFUL SOUP """
print('\n', 'Author Retrieval Beautiful Soup')
print('-------------------------------')
#create instance of soup
soup1 = BeautifulSoup(text_page1, 'html.parser')
#find all b tags
tags2 = soup1.find_all("b")
#print all b tags
for j in tags2:
    print(j.get_text())

""" AUTHOR RETRIEVAL XPATH - not finished """
print('\n', 'Author Retrieval XPath')
print('-------------------------------')

author_url = requests.get('https://agilemanifesto.org/authors.html')
tree = html.fromstring(author_url.content)
author = tree.xpath('//b')
for child in author:
    print(child.tag)

""" AGILE PRINCIPLE REGEX - not finished """
print('\n', 'Agile Principle Regex')
print('-------------------------------')
#retrieve site and convert to string
page2 = requests.get('https://agilemanifesto.org/principles.html')
text_page2 = page2.text

#use function to eliminate extra breaks in each principle
"""def normalizePrinciple(s):
    while len(re.findall(r"(<br>|<font size=\"+2\">|</font>)", s)) > 0:
        s = re.sub(r"(<br>|<font size=\"+2\">|</font>)", '', s)
    return s
#counter 
i = 0
#list of principles
principles = re.findall('', text_page2)
#while i is less than the length of principle list, print principles
while i < len(principles):
    #use the tuple to print the 1st item or the 0th part of the index
    print(principles[i])
    #increment
    i += 1 """

""" AGILE PRINCIPLE BEAUTIFUL SOUP """
print('\n', 'Agile Principle Beautiful Soup')
print('-------------------------------')
#create instance of soup
soup2 = BeautifulSoup(text_page2, 'html.parser')
#find all p tags
tags3 = soup2.find_all("p")
for h in tags3:
    print(h.get_text())

""" AGILE PRINCIPLE XPATH - not finished"""
print('\n', 'Agile Principle XPath')
print('-------------------------------')