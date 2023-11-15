from bs4 import BeautifulSoup
import requests

url = "https://market.yandex.ru/product--kholodilnik-indesit-ds-4200/1727204175/spec?track=char&sku=101627911886&cpc=HBgaRoqb-kUGxMr7Un-uSJ6GswV3Rh69TkZTWgHRTdOzIlec8sl7tfeTh1WDK72vwZwnmQyZCjOsiLfFjNQElFPE3DLP7WRdyTeSHOJsZjLegMBHQTmyqmk8XpL2bzvvFsaW_RaFJ7ZFMIGUrG-9j9LBjqKtHKkT_anr8rWUDDk1i0RMZ1gcTp8bS5rYprdkIx4yrQzP7_8tvuQAa84Zq3r2l_oEKFYfBL_rHldfE-1uJsbyW25FDONR66aV0nGFMwoiUej-tkXATJZoOs0b7A%2C%2C&uniqueId=4852853"
# url = 'https://market.yandex.ru/product--umnaia-kolonka-yandex-novaia-stantsiia-mini-umnaia-kolonka-s-alisoi/1423994419/spec'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, "lxml")

characteritics = soup.find_all('div', class_='la3zd')
for characteritic in characteritics:
    blocks = characteritic.find('div', class_="_18fxQ")
    for block in blocks:
        field_name = block.find('div', class_='_2TxqA')
        print('Поле: ', field_name.text.strip())
        field_description = block.find('div', class_='_3PnEm')
        print('Значение:', field_description.text.strip())

