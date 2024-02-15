import requests

url = "https://www.crunchbase.com/v4/data/autocompletes?query=J%3Da&collection_ids=events&limit=25&source=topSearch"

payload = {}
headers = {
  'Cookie': 'cid=Cii9GGXF2bpZSgAbsoLKAg==; __cflb=0H28vxzrpPtLNGTtMM6UPrK8jvxkeahMuGiBUwjBNZa; _pxhd=Wn/mBZ1vlgkUXYA9qeTnmUNNMBBd9GwJNVNfMQORtSbQcrilCb7unRsqioKcRuHuiazKrihiceysxUSo0L1BGA; cb_analytics_consent=granted; xsrf_token=N/aUW1NBgNw5Qy0lAHpOKBqnajIc/GyYIh4QUtzH0Bc'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
