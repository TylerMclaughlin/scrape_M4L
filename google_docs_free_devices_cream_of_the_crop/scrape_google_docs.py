import requests


def get_maxforlivedotcom_download(url):
    m4l_page = requests.get(url)
    for l in m4l_page.links:
        print(l)

doc = requests.get('https://docs.google.com/document/d/e/2PACX-1vRngItA2PEDOI3yKraeBt_kh1DLwNDeAvOL2SslmXdDBdZupjcizvszVlGvaXJcgvWMpQh4NF_boY15/pub')

all_hrefs = doc.text.split('href="')

google_link = 'https://www.google.com/url?'

for x in all_hrefs:
    if google_link in x:
        url = x.split('>')[1].split('<')[0]
        print(url)
#        if 'maxforlive.com' in url:
#            get_maxforlivedotcom_download(url)
