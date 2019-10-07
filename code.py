# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head(10)
#Code starts here



# --------------
#Code starts here





data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index, inplace=True) #drop last row
def top_ten(abc):
    country_list = []
    ids = top_countries.nlargest(10,abc)
    country_list = ids['Country_Name']
    return list(country_list)
top_10_summer = top_ten('Total_Summer')
top_10_winter = top_ten('Total_Winter')
top_10 = top_ten('Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df['Total_Summer'].plot( kind='bar')
winter_df['Total_Winter'].plot( kind='bar')
top_df['Total_Medals'].plot(kind='bar')
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()

summer_country_gold = summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'].values[0]

summer_country_gold
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()

winter_country_gold = winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'].values[0]
winter_country_gold
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio']== top_max_ratio]['Country_Name'].values[0]
top_country_gold


# --------------
#Code starts here
data_1=data.drop(data.tail(1).index)
data_1['Total_Points'] = (data_1['Gold_Total'].astype(int)*3 + data_1['Silver_Total'].astype(int)*2 + data_1['Bronze_Total'].astype(int)*1)
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
best = data[data['Country_Name']==best_country]

best = best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind='bar', stacked=True, figsize = (14,15))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)
plt.show()


