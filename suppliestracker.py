def ItemPicker():
    print ("Select an item\nSaradomin Brew(4)\nSuper Restore(4)\nSanfew Serum(4)\nDivine Super Combat(4)")
    answer = input("")
    if answer == ("Saradomin Brew(4)") or answer == ("brew") or answer == ("saradomin brew"):
        print ("How many Saradomin Brews are you using?")
        supplies = input("")
    elif answer == ("Super Restore(4)") or answer == ("restore") or answer == ("super restore"):
        print ("How many Super Restores are you using?")
        supplies = input("")
 
ItemPicker()