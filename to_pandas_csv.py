import pandas as pd
from urls import load_d
d = load_d('all_devices.pkl')
df = pd.DataFrame(d)
print(df)
df.to_csv('all_devices.csv')
