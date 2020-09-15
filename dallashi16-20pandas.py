"""Pandas CSV Reader
by
Austin McMillon"""

import pandas as pd
import numpy as np
import datetime as dt
#import sweetviz as sv
import matplotlib.pyplot as plt

resthealth = pd.read_csv('HealthInspections2016toNow.csv', index_col=0, low_memory=False)
resthealth = resthealth.reset_index()
resthealthtype = type(resthealth) #It's a dataframe
resthealthshape = resthealth.shape #R: 45844, C: 114
resthealthinfo = resthealth.info

restname = resthealth['Restaurant Name']
inscore = resthealth['Inspection Score']
indate = resthealth['Inspection Date'] 
strad = resthealth['Street Address']
intype = resthealth['Inspection Type']
resthealth['Unique Restaurant ID'] = resthealth['Restaurant Name'] + ' ' + resthealth['Street Address']
restid = resthealth['Unique Restaurant ID']        

rh = pd.concat([restid, indate, inscore, intype], axis=1)
rhshape = rh.shape

rh['Inspection Date'] = pd.to_datetime(rh['Inspection Date'])
rh['Inspection Date'] = rh['Inspection Date'].dt.strftime('%m-%d-%Y')
indate = rh['Inspection Date']
#Indate is datetime now! Clean Data!

avscore = rh.groupby(restid).mean()
#avscore's length also picks up the number of unique restaurant names in Dallas, TX. It's 7473.
#It gets the average score for each restaurant

avgscoreoa = rh['Inspection Score'].mean()

medscoreoa = rh['Inspection Score'].median()
#These two get the avg. and med. inspection scores across the entire city of Dallas.

lo_avscore = avscore.min()

hi_avscore = avscore.max()

medscore = rh.groupby(restid).median()

lo_medscore = medscore.min()

hi_medscore = medscore.max()

hiscore = rh.groupby(restid).max()

loscore = rh.groupby(restid).min()

lowestscore = loscore.min()

highestscore = hiscore.max()

"""resthealth_rpt = sv.analyze(rh)

resthealth_rpt.show_html('HealthInspections2016toNow.html')"""