from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/abs-ali560/p/N82E16883360190?Item=N82E16883360190"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

price = doc.find_all(text="$")
parent = price[0].parent
finalprice = parent.find("strong")
print(finalprice.text)