#!Python3
# NintendoUsaShop.py - Nintendo switch Usa e-shop

import requests, bs4

usaUrl = 'https://www.nintendo.com/games/game-guide/#filter/:q=&dFR[generalFilters][0]=Deals&dFR[platform][0]=Nintendo%20Switch'

usaPage = requests.get(usaUrl)
usaPage.raise_for_status

usaListPrice = []
usaListName = []

# Searching in USA e-shop
usaBs = bs4.BeautifulSoup(usaPage.text)
usaSearch = usaBs.find('div', class_="column col9 col12-tab")

print(usaSearch)



#argBs = bs4.BeautifulSoup(argPage.text)
#argSearch = argBs.find_all('div', class_='category-product-item')
#argNum = len(argSearch)

#for x in range(argNum):
#    for y in argSearch[x]:
        # Searching for game Name
#        if y == argSearch[x].find('div', class_='category-product-item-img'):
#            argNameSearch = y.find('img', class_='product-image-photo')
#            argName = argNameSearch['alt']
#            argListName.append(argName)
        # Searching for game Price
#        if y == argSearch[x].find('div', class_='category-product-item-info'):
#            argPriceSearch = y.find('span', class_='price')
#            argPriceValue = argPriceSearch.get_text()
            # Striping the "$ " value from the string
 #           argPrice = argPriceValue.strip('$ ')
 #           # Slicing the last 3 values from the string ",00"
 #           argPrice = (argPrice[:-3:])
 #           # Replacing the '.' for a nothing (delete)
 #           argPrice = argPrice.replace('.','')
 #           argListPrice.append(int(argPrice))

# Making a dict with the gamename as key and price as value
#for num in range(len(argListName)):
#    argList[argListName[num]] = argListPrice[num]
