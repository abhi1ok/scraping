import requests
from bs4 import BeautifulSoup
import random
import json
# query = entities[0].identifier.permalink
# urlApi = 'https://www.crunchbase.com/v4/data/autocompletes?query={query}&collection_ids=organizations&limit=25&source=topSearch'
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',  
]

def funtion(query):
    pass
    # hit the api
    # you will get the permalink form the api response
    # scrape_website(permalink) 

def scrape_website(url):
    user_agent = random.choice(user_agents)
    payload={}
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers,data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.text
    description = soup.find('meta', {'name': 'description'})['content']
    
    data = {
        'title': title,
        'description': description,
    }
    json_data = json.dumps(data)
    
    print(json_data)
    # permalink=""
    # requests.get(f"https://www.crunchbase.com/{permalink}")

# function call for paricular site below
scrape_website('https://www.crunchbase.com')

# fubtion(uery)
