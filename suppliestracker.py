import requests
import json
import math

url = f"https://prices.runescape.wiki/api/v1/osrs/latest"
def testFn():
    global answer
    answer = input("")
brewTotal = 0
restoreTotal = 0
def itemPicker():
    global url
    global brewTotal
    global restoreTotal
    print ("Type 'x' and hit Enter/Return to exit program")
    print ("Type 'Total' to retrieve total cost of supplies and exit program")
    print ("Select an item\nSaradomin Brew(4)\nSuper Restore(4)\nSanfew Serum(4)\nDivine Super Combat(4)")
    testFn()

    if answer == ("Saradomin Brew(4)") or answer == ("brew") or answer == ("saradomin brew"):
        brewResponse = requests.get(url)
        if brewResponse.status_code == 200:
            potionData = brewResponse.json()
            brewPrice = potionData["data"]["6685"]["high"]
            print ("Price of Saradomin Brew (4): " + str(brewPrice))
        print ("How many are you using?")
        brewSupplies = int(input(""))
        brewTotal = brewPrice * brewSupplies
        print (str(brewTotal))

    elif answer == ("Super Restore(4)") or answer == ("restore") or answer == ("super restore"):
        restoreResponse = requests.get(url)
        print (restoreResponse)
        if restoreResponse.status_code == 200:
            potionData = restoreResponse.json()
            restorePrice = potionData["data"]["3024"]["high"]
            print (restorePrice)
        print ("How many are you using?")
        supplies = int(input(""))
        restoreTotal = restorePrice * supplies
        print(str(restoreTotal))

testFn()
while not answer == ("x"):
    itemPicker()
    if answer == ("Total"):
        print ((brewTotal)+(restoreTotal))
        break