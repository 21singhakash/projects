import urllib.request
from bs4 import BeautifulSoup
import sys
import json
import rank_file
import re
import sys


# url = "https://stackoverflow.com/users/3829154/simon-p-r"
url = sys.argv[1]
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url, headers={'User-Agent': user_agent})
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html, 'html.parser')


rep = soup.find('div', attrs={'class': 'grid--cell fs-title fc-dark'}).text
clean_rep = re.sub(',', '', rep)

# g_badg = soup.find('div', attrs={'class': 'grid ai-center badge1-alternate'}).text
# s_badg = soup.find('div', attrs={'class': 'grid ai-center badge2-alternate'}).text
# b_badg = soup.find('div', attrs={'class': 'grid ai-center badge3-alternate'}).text
print(url + " has a reputation of " + clean_rep)
rank_file.rank_fun(clean_rep, url)
