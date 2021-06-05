import pickle
import requests

N_DEVICES = 7368 # as of June 4th 2021
#example: 'https://maxforlive.com/library/device/7368/unit27-sonogram'
root_url = 'https://maxforlive.com/library/device/'
dd = 'Download Device'

def get_field(text, field = "Live Version Used"):
    try:
        version = text.split(field)[1].split('>')[2].split('<')[0] 
    except IndexError:
        version = 'none'
    return version

def dict_from_url(url):
    d_dict = {}
    page = requests.get(url)
    text = page.text
    if dd in text:
        d_dict['free'] = True
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


def main():
    # iterates over all URLs up to N_DEVICES.
    # list of dicts.  each entry  contains all fields.
    all_devices = []
    for d in range(N_DEVICES): 
        url = root_url + str(d)
        d_dict = dict_from_url(url)
        all_devices.append(d_dict)
    pickle.dump(all_devices, open("all_devices.pkl", "wb"))
    
if __name__ == "__main__":

