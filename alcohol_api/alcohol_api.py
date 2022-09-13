#Rey Rivera
#Build Script 4
#
#Create a script that uses Python and/or Bash to interact specifically with an alcohol API
#Store the API information in a CSV file

import requests
import csv
#api header to access the cocktail db
headers = {
	"X-RapidAPI-Key": "0f3b396868msh838d307e1e64da3p1a590fjsnc3925cc0fb51",
	"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
}

def randomCocktail():
    url = "https://the-cocktail-db.p.rapidapi.com/random.php"
    userInput = input("Random cocktail will be generated. Press Enter to continue")
    response = requests.request("GET", url, headers=headers)
    tempJson=response.json()
    #header for the csv files
    csvHeader = ['idDrink', 'Name', 'Instructions', 'GlassType', 'Type of Drink', 'Alcoholic?']

    #loop through the json file
    dataArray = []
    for item in tempJson['drinks']:
        listing = [item['idDrink'],item['strDrink'],item['strInstructions'], item['strGlass'], item['strCategory'], item['strAlcoholic']]
        #add to an array
        dataArray.append(listing)
    with open("random.csv", 'w') as f:
        writer = csv.writer(f)

        writer.writerow(csvHeader)
        writer.writerows(dataArray)

    print('done')

def popularCocktail():
    url = "https://the-cocktail-db.p.rapidapi.com/popular.php"
    userInput = input("List of popular drinks is being retrieved. Press Enter to continue")
    response = requests.request("GET", url, headers=headers)
    tempJson=response.json()
    #header for the csv files
    csvHeader = ['idDrink', 'Name', 'Instructions', 'GlassType', 'Type of Drink', 'Alcoholic?']

    #loop through the json file
    dataArray = []
    for item in tempJson['drinks']:
        listing = [item['idDrink'],item['strDrink'],item['strInstructions'], item['strGlass'], item['strCategory'], item['strAlcoholic']]
        #add to an array
        dataArray.append(listing)
    with open("popular.csv", 'w') as f:
        writer = csv.writer(f)

        writer.writerow(csvHeader)
        writer.writerows(dataArray)
    
    print('done')

randomCocktail()
popularCocktail()
