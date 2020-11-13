import speedtest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid",rc={'axes.edgecolor':'.5'})

threads = None

s = speedtest.Speedtest()
server = int(s.get_best_server()['id'])
s.get_servers([server])
s.download(threads=threads)
s.upload(threads=threads)

results_dict = s.results.dict()

print(results_dict['ping'])

datafile = 'speed.dat' #give full path
f = open(datafile,'a')
outline = f"{results_dict['timestamp']} {results_dict['download']*1e-6} {results_dict['upload']*1e-6} {results_dict['ping']} \n"
f.write(outline)
f.close()

#plot
df = pd.read_csv(datafile,sep='\s',names=['date','download','upload','ping'])
df.date = pd.to_datetime(df.date).dt.tz_convert(tz = 'America/Phoenix')

f, axs = plt.subplots(3,1,figsize=(16, 6), sharex=True)

sns.lineplot(x="date", y="download", data=df, ax=axs[0])
axs[0].set_ylabel('download speed\n(Mbps)')
sns.lineplot(x="date", y="upload", data=df, ax=axs[1])
axs[1].set_ylabel('upload speed\n(Mbps)')
sns.lineplot(x="date", y="ping", data=df, ax=axs[2])
axs[2].set_ylabel('ping\n(ms)')
for ax in axs:
    ax.set_ylim(bottom=0)
plt.tight_layout()
plt.savefig('speed.pdf')
