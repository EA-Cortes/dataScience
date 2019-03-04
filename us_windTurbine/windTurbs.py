import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

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
print(wtCount)


# ----- # State average stats # ----- # 
outputAVG = "There are an average of " + str(avgWT) + " wind turbines per state"
print(outputAVG)
print("However, only the following states are above average")

aboveAvgStates = 0
aboveAvgWT = 0
for state in states:
	thisState = state + " has "
	filterDF = df[ df['t_state'] == state]
	windTurbs = filterDF.size/24
	
	wtList.append(windTurbs)
	#Threshhold
	if(windTurbs > avgWT):
		aboveAvgStates += 1
		aboveAvgWT += windTurbs
		thisState = thisState + str(windTurbs) + " wind turbines"
		print(thisState)

percent = 100 * (aboveAvgWT / float(totalWindTurbs))
percent = (format(percent, '.2f'))
aboveAvgOut = "There are " + str(aboveAvgStates) + " states that have more than average wind Turbines.\nThey have a combined " + str(aboveAvgWT) + " wind turbines. \nThis means they account for " + str(percent) + "% of the wind turbines"
print(aboveAvgOut)

print("")
belowAvgWT = 0
belowAvgStates = 0
for state in states:
	thisState = state + " has "
	filterDF = df[ df['t_state'] == state]
	windTurbs = filterDF.size/24
	
	#Threshhold
	if(windTurbs < 100):
		belowAvgStates += 1
		belowAvgWT += windTurbs
		thisState = thisState + str(windTurbs) + " wind turbines"
		print(thisState)


percent = 100 * (belowAvgWT / float(totalWindTurbs))
percent = (format(percent, '.2f'))
aboveAvgOut = "There are " + str(belowAvgStates) + " states have < 100 wind Turbines.\nThey have a combined " + str(belowAvgWT) + " wind turbines. \nThis means they account for " + str(percent) + "% of the wind turbines"
print(aboveAvgOut)



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