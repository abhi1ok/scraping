import requests
import json
from bs4 import BeautifulSoup

def getPerma(companyName):
    base_url=f'https://www.crunchbase.com/v4/data/autocompletes?query={companyName}&collection_ids=organizations&limit=25&source=topSearch'
    parameters = {
        "Length": 2,
        "date": 20220714
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'accept-language': 'en-US,en;q=0.9'
    }
    response = requests.get(url = base_url, params = parameters, headers = headers)
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    json_data = soup.find('script', type='application/json')
    json_obj = json.loads(json_data.text)
    for entity in json_obj['entities']:
         if entity['identifier']['value'].lower() == companyName.lower():
             return entity['identifier']['permalink']
    return None
    def scrape(perma):
        url=f'https://www.crunchbase.com/organization/{perma}'
        user_agent = random.choice(user_agents)
    
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        soup=BeautifulSoup(response.text,'html.parser')
        print(soup)



perma =getPerma("abc")
