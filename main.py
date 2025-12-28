import json
import pandas


def main():
    file_path = 'template.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    tableformatteddict = createwinsdictionary(data)

    dataframe = pandas.DataFrame(tableformatteddict)

    dataframe.index = createnewindexlabels(data)

    print(dataframe.transpose())


        
        
            
def createwinsdictionary(data):
    teamwithwinsdict = {}
    
    i = 0

    for team in data:
        wins = []
        for teamrecord in data[team].values():
            wins.append(teamrecord["W"])
        wins.insert(i, "-")
        teamwithwinsdict[team] = wins
        i += 1
    

    return teamwithwinsdict

def createnewindexlabels(data):
    teams = []
    for team in data:
        teams.append(team)
    
    return teams


    


main()