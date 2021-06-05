import pickle
import subprocess

def load_d(pkl):
    return pickle.load( open( pkl, "rb" ) )

def filter_d(ds, version, only_free = True):
    if only_free:
        ds = [d for d in ds if d['free']]
        missing_version = [d for d in ds if d['version'] == ['none']]
        print(f'{len(missing_version)} free devices are missing tested Ableton Live version info.')
    v = [d for d in ds if d['version'] == str(version)]    
    print(f'Found {len(v)} devices tested on Ableton Live version {version}.')
    return v

def open_urls(v):
    for d in v:
        subprocess.call(f'open {d["URL"]}', shell = True)
