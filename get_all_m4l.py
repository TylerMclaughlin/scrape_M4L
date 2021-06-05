import pickle
import requests

n_devices = 7368 # as of June 6th 2021
#example: 'https://maxforlive.com/library/device/7368/unit27-sonogram'
root_url = 'https://maxforlive.com/library/device/'
dd = 'Download Device'

#page = requests.get(root_url + str(2297))
#text = page.text

def get_field(text, field = "Live Version Used"):
    try:
        version = text.split(field)[1].split('>')[2].split('<')[0] 
    except IndexError:
        version = 'none'
    return version

#def main():

# list of dicts.  each entry is going to be {free, version, URL}
all_devices = []
for d in range(n_devices): 
# to debug:
#for d in range(50, 75): 
    d_dict = {}
    url = root_url + str(d)
    page = requests.get(url)
    text = page.text
    if dd in text:
        d_dict['free'] = True
        print(url)
    else:
        d_dict['free'] = False
    v = get_field(text, field = "Live Version Used")
    int_v = v.split('.')[0]
    d_dict['version'] = int_v
    
    d_dict['num_downloads'] = get_field(text, field = "Downloads")
    d_dict['tags'] = get_field(text, field = "Tags")
    d_dict['date_added'] = get_field(text, field = "Date Added")
    d_dict['device_type'] = get_field(text, field = "Device Type")
    d_dict['URL'] = url
    all_devices.append(d_dict)

pickle.dump(all_devices, open("all_devices.pkl", "wb"))
#print(text)
#if dd in text

