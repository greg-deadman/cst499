#https://www.guru99.com/accessing-internet-data-with-python.html
import urllib.request

nbaschedule = urllib.request.urlopen('https://www.espn.com/nba/schedule')


print("result code: " + str(nbaschedule.getcode()))

index = str(nbaschedule.read())
print(index[:10])
print(type(index))
print(type(str(nbaschedule)))

index2 = str(nbaschedule).find("schedule:time", 0)
print(str(nbaschedule[index2]))
'''index = str(nbaschedule.read())
print(index[:10])
index.find("schedule:time", 0)
print(nbaschedule[str(index+str(49)):str(index+str(49+7))])
print(type(str((nbaschedule))))
'''
#index = nbaschedule.find("schedule:time", 0)
#print(nbaschedule[index+49:index+56])