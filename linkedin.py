import requests
import time
from bs4 import BeautifulSoup
def scraper(query,country) :
    url = f"https://www.linkedin.com/jobs/search?keywords={query}&location={country}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

    payload = {}
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Cookie': 'bcookie="v=2&7206ff54-a0f9-4e34-843c-b31616fb82ad"; lang=v=2&lang=en-us; lidc="b=OGST05:s=O:r=O:a=O:p=O:g=2964:u=1:x=1:i=1707734448:t=1707820848:v=2:sig=AQHwlOGN6UGnYrJkhpnETdShqeq663AD"; recent_history=AQE6gQCNmv0gPwAAAY2dB8zDzh9fxOHg5Jrusun9e-y11WKvD2Ft2GaAN5H-90SwU3t5fvIeQquhgvH4CvhcrN9EGq6_g2VR-cyMS-ssESEnkOURRTRaw4TbHRyUZMgKErvzQYyfPe8rChWJPn4LAehteFoj-ZzsLVIyu4dpttLKQduSqC09Yt8-d2DNP9ommFxVlYy1O0xfHWOGH0FMCEKuVbvkCst5Fku4tILdrwTOzgLQcw1rjMav8PK9pAnAOENhxlm8N68kz8xU7fJJtG2rpOzW65sodiKhDhttVuqjVMGG9oKPe4YjYMoaAc1fnkSR-cxT5wQVUROxw_gM45VBiCMIQddK5-dKxnT0PDUakkJxJV_SzjPJCmprIJjBD7WjrM_8BW9r; JSESSIONID="ajax:1704322114510367011"; bscookie="v=1&2024021210404828db93eb-0408-4a80-8431-1976ade392dbAQGLaGxiExFtDzDhaE4PAP4srhFSjXCK"; li_rm=AQHfB6dieqvAvAAAAY2c57kDnhhRANp5Gyz-2ZRvfQGvkQm-xg5B4T-k3UIdIoaL0efj6paVJ76gENo1pqwfBQXxbMbM6Bwn_FkAc55R4XaMjdTLYiNhHHdo'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    soup=BeautifulSoup(response.text,'html.parser')
    print(response.status_code)
    print(soup)
    # print(response.text)
scraper("dev",'india')
