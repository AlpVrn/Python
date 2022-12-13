"""HATALI"""

import requests
import json

api_url= "http//api.exchangeratesapi.io/latest?base="

bozulan_doviz = input("Bozulan döviz türü : ")
alinan_doviz = input("alinan doviz türü : ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurcan : "))

result =requests.get(api_url+bozulan_doviz)

result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2}".format(miktar,bozulan_doviz,miktar * result["rates"][alinan_doviz],alinan_doviz))
