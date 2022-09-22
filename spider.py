from urllib.parse import urljoin, urlparse
import requests
import re

## '(?:href=")(.*?)"'
target_url = "http://upsssc.gov.in/"
target_link = []

def url_extractor_from(url):
    try:
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"',(response.content).decode("utf-8"))
    except TypeError:
        pass
    except requests.exceptions.InvalidURL:
        pass


def crawl(url):
    href_link = url_extractor_from(url)
    for link in href_link:
       link = urljoin(url,link)

       if "#" in link:   ## Avoid the # link
            link = link.split("#")[0]
        
       if target_url in link and link not in target_link: ## find only unique link
            target_link.append(link)
            print(link)
            crawl(link)   ## recursive  function to map whole website across i,e find hidden link
    

crawl(target_url)





