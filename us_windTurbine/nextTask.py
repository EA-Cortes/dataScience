import pandas as pd 

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
	print(output)
	purchaseList = []
	print("Year - Number of wind turbines bought")
	for year in range(minYear, maxYear+1):
		filterDF = state_df[ state_df['p_year'] == year]
		windTurbs = filterDF.size/24
		n = windTurbs
		# purchaseList.append((year, windTurbs))
		innerO = "" + str(year) + " - " + str(windTurbs)
		print(innerO)
		purchaseList.append([year, windTurbs])
	# print(purchaseList)
	return purchaseList


TXList = purchasedByYear("TX")
CAList = purchasedByYear("CA")
ILList = purchasedByYear("IL")

# ------ # Function that pads the list for easier output # ------ # 
def padLists(lists):
	longest = 0
	for item in lists:
		if(len(item) > longest):
			longest = len(item)
	# print(longest)

	appYear = 0
	for item in lists:
		if(len(item) < longest):
			appYear = item[0][0]
			print(appYear)
			item.reverse()
			while(len(item) < longest):
				item.append([appYear, 0])
				appYear -= 1
			item.reverse()
			# print(item)

padLists([TXList, CAList, ILList])

print("\nFormatted and padded")
print(TXList)
print("")
print(CAList)
print("")
print(ILList)