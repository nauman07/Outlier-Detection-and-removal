import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Crop_recommendation.csv")
df.head()
#Univariate outlier detection
df['N'].plot.box()
plt.savefig('N.png')
plt.close()
df['P'].plot.box()
plt.savefig('P.png')
plt.close()
df['K'].plot.box()
plt.savefig('K.png')
plt.close()
df['temperature'].plot.box()
plt.savefig('temp.png')
plt.close()
df['humidity'].plot.box()
plt.savefig('humid.png')
plt.close()
df['ph'].plot.box()
plt.savefig('ph.png')
plt.close()
df['rainfall'].plot.box()
plt.savefig('rain.png')
plt.close()
#Bivariate outlier detection
df.plot.scatter('N', 'P')
plt.savefig('N_p.png')
plt.close()
df.plot.scatter('N', 'K')
plt.savefig('N_K.png')
plt.close()
df.plot.scatter('N', 'temperature')
plt.savefig('N_temp.png')
plt.close()
df.plot.scatter('N', 'humidity')
plt.savefig('N_humid.png')
plt.close()
df.plot.scatter('N', 'ph')
plt.savefig('N_ph.png')
plt.close()
df.plot.scatter('N', 'rainfall')
plt.savefig('N_rain.png')
plt.close()
df.plot.scatter('P', 'K')
plt.savefig('P_K.png')
plt.close()
df.plot.scatter('P', 'temperature')
plt.savefig('P_temp.png')
plt.close()
df.plot.scatter('P', 'humidity')
plt.savefig('P_humid.png')
plt.close()
df.plot.scatter('P', 'ph')
plt.savefig('P_ph.png')
plt.close()
df.plot.scatter('P', 'rainfall')
plt.savefig('P_rainfall.png')
plt.close()
df.plot.scatter('K', 'temperature')
plt.savefig('K_temp.png')
plt.close()
df.plot.scatter('K', 'humidity')
plt.savefig('K_humid.png')
plt.close()
df.plot.scatter('K', 'ph')
plt.savefig('K_ph.png')
plt.close()
df.plot.scatter('K', 'rainfall')
plt.savefig('K_rainfall.png')
plt.close()
df.plot.scatter('temperature', 'humidity')
plt.savefig('temp_humid.png')
plt.close()
df.plot.scatter('temperature', 'ph')
plt.savefig('temp_ph.png')
plt.close()
df.plot.scatter('temperature', 'rainfall')
plt.savefig('temp_rain.png')
plt.close()
df.plot.scatter('humidity', 'ph')
plt.savefig('hum_ph.png')
plt.close()
df.plot.scatter('humidity', 'rainfall')
plt.savefig('hum_rainfall.png')
plt.close()
#Histogram Analysis
df['N'].plot.hist()
plt.savefig('N_hist.png')
plt.close()
df['P'].plot.hist()
plt.savefig('P_hist.png')
plt.close()
df['K'].plot.hist()
plt.savefig('K_hist.png')
plt.close()
df['temperature'].plot.hist()
plt.savefig('temp_hist.png')
plt.close()
df['humidity'].plot.hist()
plt.savefig('humid_hist.png')
plt.close()
df['ph'].plot.hist()
plt.savefig('ph_hist.png')
plt.close()
df['rainfall'].plot.hist()
plt.savefig('rain_hist.png')
plt.close()
#Correlation Diagram
cor = df.corr()
plt.figure(figsize=(16,10))
sns.heatmap(cor)
plt.savefig("heatmap.png")
plt.close()
