class NFLTeam:
    name = ""
    city = ""
    state = ""
    pointsInLastGame = 0
    avgPointsPerGame = 0.0

    def __init__(self, name, city, state, pointsInLastGame, avgPoints):
        self.name = name
        self.city = city
        self.state = state
        self.pointsInLastGame = pointsInLastGame
        self.avgPointsPerGame = avgPoints

    def printNameCityState(self):
        print(self.name + " " + self.city + ", " + self.state)

teams = []
teams.append(NFLTeam("Colts", "Indianapolis", "Indiana", 17, 14.8))
teams.append(NFLTeam("Bills", "Buffalo", "New York", 27, 32.6))
teams.append(NFLTeam("Jets", "New York", "New York", 4, 3.0))

#Imperative Programming
for t in teams:
    if t.state == "New York":
        t.printNameCityState()

print("----------")

newYorkTeams = filter(lambda team: team.state != "New York", teams)

#Declarative Programming
for t in newYorkTeams:
    t.printNameCityState()

print("Hello")