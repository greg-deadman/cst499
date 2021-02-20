#used pip install lxml to retrieve lxml library
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

"""root = etree.Element('root')
print(root.tag)"""

page = requests.get('https://www.google.com/finance')
text_page = page.text

""" DOW JONES REGEX """
#search allows us to find the expressions we are looking for in the text; x and y only require one matching group to find a good expression, z took three to get the correct spot
x = re.search('class="[a-zA-Z|\d]{3,6}">([a-zA-Z|\s]{3,9})<\/div>', text_page)
y = re.search('aria-label="([a-zA-Z]{2,4})\s(by)\s(\S{3,7})"><div', text_page)
z = re.search('P2Luy (Ebnabc|Ez2Ioe)">([+-]?)([0-9]*.?[0-9]{1,})</span>(</div>){4}.{1,70}Dow Jones', text_page)

#concatenate the print to get the first task, print groups for each search; need to use group(2) for access to the correct number due to increase in number of matching groups
print('The ' + x.group(1) + ' is ' + y.group(1) + ' ' + y.group(2) + ' ' + y.group(3) + ' or ' + z.group(2) + z.group(3) + ' points' + '.')

""" DOW JONES BEAUTIFUL SOUP """
soup = BeautifulSoup(text_page, 'html.parser')
print('The', soup.find(string=re.compile("Dow Jones")), 'is', )
#print('The ') + print(soup.find(string=re.compile("Dow Jones"))) + print(' is ') + print(soup.find(string=re.compile("Up by" or "Down by")))

""" DOW JONES XPATH """

""" AUTHOR RETRIEVAL REGEX """

""" AUTHOR RETRIEVAL BEAUTIFUL SOUP """

""" AUTHOR RETRIEVAL XPATH """

""" AGILE PRINCIPLE REGEX """

""" AGILE PRINCIPLE BEAUTIFUL SOUP """

""" AGILE PRINCIPLE XPATH """