'''the only python features used to solve assignment 3. 
created a function
used a while loop
used len to get length of list
regular expression
regex sub and capture
re.sub(regex, string)'''

import requests
import re

page = requests.get('https://www.google.com/finance')
text_page = page.text

#search allows us to find the expressions we are looking for in the text; x and y only require one matching group to find a good expression, z took three to get the correct spot
x = re.search('class="[a-zA-Z|\d]{3,6}">([a-zA-Z|\s]{3,9})<\/div>', text_page)
#doesn't take into account down by
#y = re.search('aria-label="(Up by \S{3,7})"><div', text_page)
z = re.search('P2Luy Ez2Ioe">([+-]?)([0-9]*.?[0-9]{1,})</span>(</div>){4}.{1,70}Dow Jones', text_page)

"""
test code
print(x.group(1))
print(y.group(1))
print(z.group(2))
"""

#concatenate the print to get the first task, print groups for each search; need to use group(2) for access to the correct number due to increase in number of matching groups
#print('The ' + x.group(1) + ' is ' + 'y.group(1)' + ' or ' + z.group(2) + ' points')

#counter
i = 0
#list of companies you may be interested in
companies = re.findall('(ZvmM7">)(.{1,50})(</div>){3}', text_page)
#while i is less than the length of company list, print company
while i < len(companies):
    #use the tuple to print the 2nd item or 2nd matching group in the array/regex (0 is the class ZvmM7, 1 is the company name, 2 is the third matching group)
    print(companies[i][1])
    #counter
    i += 1

#XPath expressions - using sub, I'm not sure how to make this a better process 
"""test = re.sub(r"@name=\"", '', '/content/folder[@name="Greg"]/folder[@name="CST499"]/report[@name="Greg Report"]')
test2 = re.sub(r"\[", '/', test)
test3 = re.sub(r"\"", '', test2)
test4 = re.sub(r"\]", '', test3)
print(test)
print(test2)
print(test3)
print(test4)"""

s1 = '/content/folder[@name="Greg"]/folder[@name="CST499"]/report[@name="Greg Report"]'
def normalizeName(s):
    while len(re.findall(r"(folder|report)\[@name=['\"](.*?)['\"]\]", s))>0:
        s = re.sub(r"(folder|report)\[@name=['\"](.*?)['\"]\]", r'\2', s)
    return s

#s = '/content/folder[@name="Greg"]/folder[@name="CST499"]/report[@name="Greg Report"]'
print(normalizeName(s1))