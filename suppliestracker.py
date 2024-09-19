import requests

url = f"https://prices.runescape.wiki/api/v1/osrs/latest"
def answerFn():
    global answer
    answer = input("")
brewTotal = restoreTotal = sanfewTotal = divineTotal = 0
def itemPicker():
    global url, brewTotal, restoreTotal, sanfewTotal, divineTotal
    print ("Type 'x' and hit Enter/Return to exit program")
    print ("Type 'total' to retrieve total cost of supplies and exit program")
    print ("Select an item\n1. Saradomin Brew(4)\n2. Super Restore(4)\n3. Sanfew Serum(4)\n4. Divine Super Combat(4)")
    answerFn()

    if answer == ("Saradomin Brew(4)") or answer == ("brew") or answer == ("saradomin brew") or answer == ("1"):
        brewResponse = requests.get(url)
        if brewResponse.status_code == 200:
            potionData = brewResponse.json()
            brewPrice = potionData["data"]["6685"]["high"]
            print ("Price of Saradomin Brew (4): " + str(brewPrice))
        print ("How many are you using?")
        brewSupplies = int(input(""))
        brewTotal = brewPrice * brewSupplies
        print (str(brewTotal))

    elif answer == ("Super Restore(4)") or answer == ("restore") or answer == ("super restore") or answer == ("2"):
        restoreResponse = requests.get(url)
        if restoreResponse.status_code == 200:
            potionData = restoreResponse.json()
            restorePrice = potionData["data"]["3024"]["high"]
            print ("Price of Super Restore (4): " + str(restorePrice))
        print ("How many are you using?")
        supplies = int(input(""))
        restoreTotal = restorePrice * supplies
        print(str(restoreTotal))
    
    elif answer == ("Sanfew Serum(4)") or answer == ("sanfew") or answer == ("sanfew serum") or answer == ("3"):
        sanfewResponse = requests.get(url)
        if sanfewResponse.status_code == 200:
            potionData = sanfewResponse.json()
            sanfewPrice = potionData["data"]["10925"]["high"]
            print ("Price of Sanfew Serum (4): " + str(sanfewPrice))
        print ("How many are you using?")
        supplies = int(input(""))
        sanfewTotal = sanfewPrice * supplies
        print(str(sanfewTotal))
    
    elif answer == ("Divine Super Combat(4)") or answer == ("divine super combat") or answer == ("4") or answer == ("divine scb"):
        divineResponse = requests.get(url)
        if divineResponse.status_code == 200:
            potionData = divineResponse.json()
            divinePrice = potionData["data"]["23685"]["high"]
            print ("Price of Divine Super Combat Potion(4): " + str(divinePrice))
        print ("How many are you using?")
        supplies = int(input(""))
        divineTotal = divinePrice * supplies
        print(str(divineTotal))

answerFn()
while not answer == ("x"):
    itemPicker()
    if answer == ("total"):
        print ("Total cost of supplies: "+ str((brewTotal)+(restoreTotal)+(sanfewTotal)+(divineTotal)))
        break