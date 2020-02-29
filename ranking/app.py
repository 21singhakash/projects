import urllib.request
from bs4 import BeautifulSoup
import rank_file
import re

# @akash_singh
# app_func(url) method creates a request to read a html page & calls rank_func.
def app_func(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url, headers={'User-Agent': user_agent})
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html, 'html.parser')
    rep = soup.find('div', attrs={'class': 'grid--cell fs-title fc-dark'}).text
    clean_rep = re.sub(',', '', rep)
    rank_file.rank_func(clean_rep, url)
