#!/Users/keatonb/anaconda3/bin/python

import speedtest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid",rc={'axes.edgecolor':'.5'})

servers = [1782] #Seattle
threads = None

s = speedtest.Speedtest()
s.get_servers(servers)
s.download(threads=threads)
s.upload(threads=threads)

results_dict = s.results.dict()

datafile = '/Users/keatonb/speed.dat' #give full path
f = open(datafile,'a')
outline = f"{results_dict['timestamp']} {results_dict['download']*1e-6} {results_dict['upload']*1e-6} \n"
f.write(outline)
f.close()

#plot
df = pd.read_csv(datafile,sep='\s',names=['date','download','upload'])
df.date = pd.to_datetime(df.date).dt.tz_convert(tz = 'America/Los_Angeles')

f, axs = plt.subplots(2,1,figsize=(11, 6), sharex=True)

sns.lineplot(x="date", y="download", data=df, ax=axs[0])
axs[0].set_ylabel('download speed\n(Mbps)')
sns.lineplot(x="date", y="upload", data=df, ax=axs[1])
axs[1].set_ylabel('upload speed\n(Mbps)')
for ax in axs:
    ax.set_ylim(bottom=0)
plt.tight_layout()
plt.savefig('/Users/keatonb/speed.pdf')
