import requests
import json
 
url = "https://api.travelpayouts.com/v2/prices/month-matrix"
 
querystring = {"currency":"usd","show_to_affiliates":"true","origin":"LED","destination":"HKT"}
 
headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}
 
response = requests.request("GET", url, headers=headers, params=querystring)
 
#store the input and load it into a dictionary using the loads function
json_input = json.loads(response.text)

#extract the list at key pair data in the dictionary
data_list = json_input["data"]

#create 2 empty stacks to store data to later return
lessThan650 = []
greaterThan650 = []

#traverse through the list in the extracted earlier
for i in range(0, len(data_list)):
    #check for less than 650 at value key pair
    if (int(data_list[i]["value"]) <= 650):
        #populate stack with valid dictionary from list
        lessThan650.append(data_list[i])
    #check for greater than 650 at value key pair
    if (int(data_list[i]["value"]) > 650):
        #populate stack with valid dictionary from list
        greaterThan650.append(data_list[i])

#Generate a menu for user input to select what option they want
running = True
while (running):
    userInput = input("Enter 0 if you would like to see the flights less than 650 \nEnter 1 if you would like flights for more than 650\nEnter anything else to exit code:")
    if userInput == '0':
        print(lessThan650, "\n\n")
    if userInput == '1':
        print(greaterThan650, "\n\n")
    if userInput != '0' and userInput != '1':
        print("\n\nExiting code")
        running = False

