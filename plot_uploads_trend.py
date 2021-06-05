import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('all_devices.csv')
free = df[(df.version != 'none') & df.free]
free['datetime_added'] = pd.to_datetime(free.date_added)
free['datetime_added'].groupby([free['datetime_added'].dt.year]).count().plot(kind="bar", color = '#494949')
plt.title('Number of free Max for Live devices uploaded to maxforlive.com, by year')
plt.ylabel('Devices uploaded')
plt.show()
