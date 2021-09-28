import requests
from bs4 import BeautifulSoup
import urllib.request
import os



with open(r"C:\Users\user\Desktop\pyparser\list.txt", 'a', encoding='utf-8') as file:
    for x in range(1, 45):
        url = 'https://www.russianfood.com/recipes/bytype/?fid=260&page={}#rcp_list'.format(x)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        print(x)
        items = soup.find_all('div', class_='recipe_l')
        for n, i in enumerate(items, start =1):
            itemName = i.find('div', class_='title').text.strip()
            itemPrice = i.find('div', class_='ingr_str').text.strip()
            photo = i.find(class_ = "foto")
            image = photo.find("img")
            if itemPrice is None:
               break
            else:
                if image is None:
                    file.write(str(n) + ": " + itemName + '\n' + 'Ингридиенты:' + itemPrice + '\n' + 'Имя картинки:' +  itemName + '\n')
                    print("Скачиваю {}".format(itemName))
                else:
                    source=image.get("src")
                    relurl = 'https:' + source
                    img_name = str(source.split('/')[-1])
                    file.write(str(n) + ": " + itemName + '\n' + 'Ингридиенты:' + itemPrice + '\n' + 'Имя картинки:' +  itemName + '\n')
                    print("Скачиваю {}".format(itemName))
                    formatName = itemName.replace(" ", "_")
                    readyName = formatName.replace('"', '_')
                    urllib.request.urlretrieve(relurl, os.path.join(readyName + '.png'))

                if n == 20:
                    break

