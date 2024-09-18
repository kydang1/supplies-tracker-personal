import requests
import json
import math

url = f"https://prices.runescape.wiki/api/v1/osrs/latest"

def ItemPicker():
    global url
    print ("Select an item\nSaradomin Brew(4)\nSuper Restore(4)\nSanfew Serum(4)\nDivine Super Combat(4)")
    answer = input("")
    if answer == ("Saradomin Brew(4)") or answer == ("brew") or answer == ("saradomin brew"):
        SaradominBrew4response = requests.get(url)
        print (SaradominBrew4response)
        if SaradominBrew4response.status_code == 200:
            potionData = SaradominBrew4response.json()
            SaradominBrew4Price = potionData["data"]["6685"]["high"]
            print (SaradominBrew4Price)
        print ("How many are you using?")
        supplies = int(input(""))
    TotalCost = SaradominBrew4Price * supplies
    print ("Total Cost:")
    print (TotalCost)

ItemPicker()