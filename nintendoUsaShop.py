#!Python3
# switchDealsArg - Nintendo switch argentina eshop deals

import requests, bs4
# aksdasd testing

#priceInput = input('Please enter a price: ')

argUrl = 'https://store.nintendo.com.ar/?cid=L001-01:ch=pmpd'
usaUrl = 'https://www.nintendo.com/games/game-guide/#filter/:q=&dFR[platform][0]=Nintendo%20Switch'
dolarUrl = 'https://www.dolarhoy.com/'

usaPage = requests.get(usaUrl)
usaPage.raise_for_status

usaListPrice = []
usaListName = []

# Searching in USA e-shop
usaBs = bs4.BeautifulSoup(usaPage.text)
usaSearch = usaBs.find_all('a', class_='main_link')

for x in usaSearch:
    




argBs = bs4.BeautifulSoup(argPage.text)
argSearch = argBs.find_all('div', class_='category-product-item')
argNum = len(argSearch)

for x in range(argNum):
    for y in argSearch[x]:
        # Searching for game Name
        if y == argSearch[x].find('div', class_='category-product-item-img'):
            argNameSearch = y.find('img', class_='product-image-photo')
            argName = argNameSearch['alt']
            argListName.append(argName)
        # Searching for game Price
        if y == argSearch[x].find('div', class_='category-product-item-info'):
            argPriceSearch = y.find('span', class_='price')
            argPriceValue = argPriceSearch.get_text()
            # Striping the "$ " value from the string
            argPrice = argPriceValue.strip('$ ')
            # Slicing the last 3 values from the string ",00"
            argPrice = (argPrice[:-3:])
            # Replacing the '.' for a nothing (delete)
            argPrice = argPrice.replace('.','')
            argListPrice.append(int(argPrice))

# Making a dict with the gamename as key and price as value
for num in range(len(argListName)):
    argList[argListName[num]] = argListPrice[num]

# Getting the final dolar price + taxes
precioDolar = dolarVenta + (dolarVenta * 0.29)

for x in range(len(argListName)):
    print(argListName[x] + " " + "$ " + str(argListPrice[x]) + ", en dolares seria: U$S " + str("{:.2f}".format(argListPrice[x]/precioDolar)) + "\n")

# Searching in USA e-shop
#usaBs = bs4.BeautifulSoup(usaPage.text)
#usaSearch = usaBs.find('div', {'id':'games-list-container'})