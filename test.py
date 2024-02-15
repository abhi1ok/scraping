# hit the url api
# get the response 
# get the permalinkn form the response 
# pass that permlink to your existing scraper funtion url-''https://www.crunchbase.com/{permalink}''
# print json


# step1 :
import requests

url = "https://www.crunchbase.com/organization/jar-09f5"
headers = {
    "authority":"www.crunchbase.com",
    "Cookie":
    "cb_analytics_consent=granted; cid=CihG6WXDMW5vygAbnO/KAg==; featureFlagOverride=%7B%7D; featureFlagOverrideCrossSite=%7B%7D; _pxvid=db196e61-c5e7-11ee-9712-ef58df46755b; __cflb=0H28vxzrpPtLNGTtMM6UPrK8jvxkeaiK8MhW1Egmjvk; pxcts=64b6d442-c737-11ee-8cd6-a563b01f8e83; xsrf_token=d4unAjPDjziI+HWsA7TVATevlvsuN6JUvZ/oOLMcuBE; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+09+2024+16%3A24%3A42+GMT%2B0530+(India+Standard+Time)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _pxhd=IZIlhPhajmLg/tl1ihkYc5LBd9LSbL-W9vZddsJPdwVIXe1qWnKkIfRC2WgzS9wXpzdSIVZKEqCe1/MrcJiGMw",

    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
      }

payload = {}
headers = {'User-Agent': user_agents}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
