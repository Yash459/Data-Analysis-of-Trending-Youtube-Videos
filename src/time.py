import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def videos_time(df):
	
	sz = len(df)
	
	dic = {}
	for e in df:
		p_time = [int(x[11:13]) for x in list(df[e].publish_time)]
		video_counter = [0]*24
		for j in p_time:
			video_counter[j] += 1
		dic[e] = video_counter
	frame = pd.DataFrame(dic)
	sns.set(style="whitegrid")
	time_video = sns.lineplot(data=frame, palette="tab10", linewidth=1.5)
	time_video.set_title('Published Videos in 24 Hours')
	time_video.set_xlabel('Hours')
	time_video.set_ylabel('Published Videos')
	plt.show()
	
dflist = {}
csv = pd.read_csv('../datasets/USvideos.csv')
dflist['US'] = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/DEvideos.csv')
dflist['DE'] = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/CAvideos.csv')
dflist['CA'] = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/FRvideos.csv')
dflist['FR'] = pd.DataFrame(csv)
csv = pd.read_csv('../datasets/GBvideos.csv')
dflist['GB'] = pd.DataFrame(csv)
videos_time(dflist)


