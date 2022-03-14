pip install requests
pip install bs4

import requests
import bs4

from bs4 import BeautifulSoup as bs

github_user= input("Enter the User Name:")
url="https://github.com/"+github_user

r=requests.get(url)

soup=bs(r.content, 'html.parser')
img=soup.find('img', {'alt' : 'Avatar'})['src']

print("Link "+img)
