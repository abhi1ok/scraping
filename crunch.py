import requests

from bs4 import BeautifulSoup
webUnblocker={
  "http":"http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
  "https":"http://USERNAME:PASSWORD@unblock.oxylabs.io:60000"
  }
response=requests.get(
    "https://www.crunchbase.com/organization/jar-09f5",
    verify=False,
    proxies=webUnblocker,
)
print(response.status_code)