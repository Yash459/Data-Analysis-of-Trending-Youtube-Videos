import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def videos_time(df):
	'''
	Show the fluctuation publishing videos in 24 Hours within 5 different area
	'''
	sz = len(df)
	dic = {}
	for e in df:
		p_time = [int(x[11:13]) for x in list(df[e].publish_time)] # extract the hour from dataframe
		video_counter = [0]*24
		for j in p_time: # count the videos in each hour
			video_counter[j] += 1
		dic[e] = video_counter # add the timetable into dictionary
	frame = pd.DataFrame(dic)
	sns.set(style="whitegrid")
	fig = sns.lineplot(data=frame, palette="tab10", linewidth=1.5)
	fig.set_title('Publishing Videos in 24 Hours')
	fig.set_xlabel('Hours')
	fig.set_ylabel('Publishing Videos')
	plt.xticks(np.arange(0, 24, 1))
	plt.yticks(np.arange(0, 7000, 1000))
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


