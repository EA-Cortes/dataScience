import math
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.lines import Line2D
from collections import namedtuple

f = open("output.txt", "w")
f = open("output.txt", "a")

# ----- # State Abbreviations # ----- # 
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# ----- # Input Data # ----- # 
df = pd.read_csv("uswtdb_v1_3_20190107.csv")


wtList = []					# List of wint Turbines per state
totalWindTurbs = 0			# Count the total wind turbines
# Filter data by states
for state in states:
	thisState = state + " has "
	filterDF = df[ df['t_state'] == state]
	windTurbs = filterDF.size/24
	wtList.append(windTurbs)
	totalWindTurbs += windTurbs
	thisState = thisState + str(windTurbs) + " wind turbines"
	# print(thisState)


avgWT = sum(wtList)/len(wtList)
wtCount = "There are a total of " + str(totalWindTurbs) + " wind turbines in the US!"
f.write(wtCount)

wtStdv = []
sumWT = 0 
for state in wtList:
	diff = ((state - avgWT)**2)
	wtStdv.append(diff)
	sumWT += diff
	
# print(wtList)
var = sumWT/float(len(states))
std = math.sqrt(var)	
# print(std)


# ----- # State average stats # ----- # 
outputAVG = "\nThere are an average of " + str(avgWT) + " wind turbines per state"
f.write(outputAVG)
f.write("\nHowever, only the following states are above average")

aboveAvgWT = 0
aboveAvgStates = 0
sufficientWT = 0
sufficientStates = 0
belowAvgWT = 0
belowAvgStates = 0
superLowWT = 0
superLowStates = 0
for state in states:
	thisState = "\n" + state + " has "
	filterDF = df[ df['t_state'] == state]
	windTurbs = filterDF.size/24
	
	#Threshhold
	if(windTurbs > 990):
		sufficientStates += 1
		sufficientWT += windTurbs
		thisState = thisState + str(windTurbs) + " wind turbines! "
		f.write(thisState)

	#Threshhold
		if(windTurbs > avgWT):
			aboveAvgStates += 1
			aboveAvgWT += windTurbs
			thisState = thisState + str(windTurbs) + " wind turbines"
	#Threshhold
	if(windTurbs < 100):
		if(windTurbs < 50):
			superLowStates += 1
			superLowWT += windTurbs
			thisState = thisState + str(windTurbs) + " wind turbines"
			# print(thisState)
		else:
			belowAvgStates += 1
			belowAvgWT += windTurbs
			thisState = thisState + str(windTurbs) + " wind turbines"
			# print(thisState)
	#Threshhold
	if(windTurbs < 50):
		belowAvgStates += 1
		belowAvgWT += windTurbs
		thisState = thisState + str(windTurbs) + " wind turbines"
		# print(thisState)

# ----- # Output results # ----- #
percent = 100 * (aboveAvgWT / float(totalWindTurbs))
percent = (format(percent, '.2f'))
aboveAvgOut = "\n\nThere are " + str(aboveAvgStates) + " states that have more than average wind Turbines.\nThey have a combined " + str(aboveAvgWT) + " wind turbines. \nThis means they account for " + str(percent) + "% of the wind turbines"
f.write(aboveAvgOut)

percent = 100 * (sufficientWT / float(totalWindTurbs))
percent = (format(percent, '.2f'))
aboveAvgOut = "\n\nThere are " + str(sufficientStates) + " states that have more 1000 wind Turbines.\nThey have a combined " + str(sufficientWT) + " wind turbines. \nThis means they account for " + str(percent) + "% of the wind turbines"
f.write(aboveAvgOut)

percent = 100 * (belowAvgWT / float(totalWindTurbs))
percent = (format(percent, '.2f'))
belowAvgOut = "\n\nThere are " + str(belowAvgStates) + " states have < 100 wind Turbines.\nThey have a combined " + str(belowAvgWT) + " wind turbines. \nThis means they account for " + str(percent) + "% of the wind turbines"
f.write(belowAvgOut)

percent = 100 * (superLowWT / float(totalWindTurbs))
percent = (format(percent, '.2f'))
superLowOut = "\n\nThere are " + str(superLowStates) + " states have < 50 wind Turbines.\nThey have a combined " + str(superLowWT) + " wind turbines. \nThis means they account for " + str(percent) + "% of the wind turbines"
f.write(superLowOut)

# Bar graph
n_groups = 51
x = np.arange(n_groups)
mean = []
for state in states:
	mean.append(avgWT)

def getBarColor():
	colList = []
	for wt in wtList:
		if wt > avgWT:
			colList.append('g')
		elif (wt > 900):
			colList.append('c')
		elif(wt > 300):
			colList.append('b')
		else:
			colList.append('r')
	return colList

def getN():
	colList = []
	for wt in wtList:
		if wt > avgWT:
			colList.append('Above Average')
		elif (wt > 900):
			colList.append('Slightly below average')
		elif(wt > 300):
			colList.append('Above 300')
		else:
			colList.append('Needs improvement')
	return colList

def thousands(x, pos):
    'The two args are the value and tick position'
    return '%1.0f' % (x * 1)
formatter = FuncFormatter(thousands)

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_title('Wind Turbines in the US by state')
ax.set_xlabel('States')
ax.set_ylabel('# of wind turbines')
ax.yaxis.set_major_formatter(formatter)
plt.bar(x, wtList, color=getBarColor(), alpha=0.7)
plt.xticks(x, states)
plt.plot(mean, 'k--')

green_patch = mpatches.Patch(color='g', label='Above average')
cyan_patch = mpatches.Patch(color='c', label='Slightly below average')
blue_patch = mpatches.Patch(color='b', label='Below average')
red_patch = mpatches.Patch(color='r', label='Needs significant imrpovement')
white_patch =mpatches.Patch(color='w', label='Do these states even care about the planet?')
mean_line = Line2D([0], [0], color='k', lw=2, label='Average wind turbines', linestyle='--')
plt.legend(loc='upper left', handles=[green_patch, cyan_patch, blue_patch, red_patch, white_patch, mean_line])



plt.show()

# The following may be useful to analyze the data using different parameters
# ----- # Data Types # ----- #
# Case_ID
# Fea_ors
# usgs_pr_id
# t_state
# t_county
# t_fips 
# p_name
# p_year
# p_num
# p_cap
# t_manu
# t_model
# t_cap
# t_hh
# t_rd
# t_rsa
# t_ttlh
# t_conf_atr
# t_conf_loc
# t_img_date
# t_img_srce
# xlong
# ylat