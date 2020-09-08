#!Python3
# switchDealsArg - Nintendo switch argentina eshop deals

import requests, bs4
# aksdasd testing

#priceInput = input('Please enter a price: ')

argUrl = 'https://store.nintendo.com.ar/?cid=L001-01:ch=pmpd'
usaUrl = 'https://www.nintendo.com/games/game-guide/#filter/:q=&dFR[platform][0]=Nintendo%20Switch'
dolarUrl = 'https://www.dolarhoy.com/'
argPage = requests.get(argUrl)
argPage.raise_for_status
usaPage = requests.get(usaUrl)
usaPage.raise_for_status
dolarPage = requests.get(dolarUrl)
dolarPage.raise_for_status

argListPrice = []
argListName = []
argList = {}
dolarVenta = ''

# Searching for ARG dolar value
dolarBs = bs4.BeautifulSoup(dolarPage.text)
dolarSearch = dolarBs.find('a', href='/cotizaciondolaroficial')
dolarParent = dolarSearch.parent.parent

for parent in dolarParent:
    for par in parent:
        parSearch = dolarParent.find_all('div', class_='col-6 text-center')
for x in range(len(parSearch)):
    if parSearch[x].small.text == 'VENTA':
        dolarNum = parSearch[x].span.text
        # Taking the "$" away
        dolarVenta = (dolarNum.strip('$ '))
        # Changing the "," for a "." and changing it to a float number
        dolarVenta = float(dolarVenta.replace(',','.'))


# Searching in ARG e-shop
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





# ---------------------------------------------------------------------------
#nbs4 = bs4.BeautifulSoup(npage.text)
#nprice = nbs4.find_all('span', class_='price')
#nname = nbs4.find_all('a', class_='category-product-item-title-link')

#nimage = nbs4.find('img', class_='product-image-photo')

#print(nimage['alt'])

#print("Intentando 02")

#nlistprice = []
#for x in nprice:
#    nlistprice.append(x.get_text())
#nlistname = []


