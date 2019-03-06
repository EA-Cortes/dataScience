import pandas as pd 

f = open("annualPurchasedByState.txt", "w")
f = open("annualPurchasedByState.txt", "a")


df = pd.read_csv("uswtdb_v1_3_20190107.csv")



# print(df.dtypes)
# print(df.head())


# df_sub = fl_df[ df['p_year'] < 2000]
# df_avgPurchaseYear =  fl_df
# print(df_avgPurchaseYear)
# print(df_sub)
# print("Formatted")

def purchasedByYear(state):
	state_df = df[ df['t_state'] == state]
	minYear = int(state_df['p_year'].min())
	maxYear = int(state_df['p_year'].max())
	output = "\nThe first wind turbine in " + state + " was purchased in: " + str(minYear) + ". The most recent was purchased in: " + str(maxYear) + ""
	f.write(output)
	purchaseList = []
	f.write("\nYear - Number of wind turbines bought")
	for year in range(minYear, maxYear+1):
		filterDF = state_df[ state_df['p_year'] == year]
		windTurbs = filterDF.size/24
		n = windTurbs
		# purchaseList.append((year, windTurbs))
		innerO = "\n" + str(year) + " - " + str(windTurbs)
		f.write(innerO)
		purchaseList.append([year, windTurbs])
	# print(purchaseList)
	return purchaseList

# 
# TXList = purchasedByYear("TX")
# CAList = purchasedByYear("CA")
# ILList = purchasedByYear("IL")


# ------ # Function that pads the list for easier output # ------ # 
def padLists(lists):
	longest = 0
	for item in lists:
		# print(len(item))
		if(len(item) > longest):
			longest = len(item)
	# print(longest)

	appYear = 0
	nn = 1
	for item in lists:
		
		if(len(item) < longest):
			
			appYear = item[0][0]
			item.reverse()
			while(len(item) < longest+1):
				item.append([appYear, 0])
				appYear -= 1
			item.reverse()

		nn += 1


def getByState(states):
	# print("Get by state)")
	
	purchasedList = []
	tempList = []
	for state in states:
		tempList.append(purchasedByYear(state))
	
	padLists(tempList)
	stateList = []
	i = 0
	for state in states:
		stateList.append([state, tempList[i]])
		i += 1
	
	
	for s in stateList:
		f.write("\n\n")
		f.write(str(s))


	return purchasedList
	