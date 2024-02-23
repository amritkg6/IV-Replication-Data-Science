import pandas as pd

# Load the datasets
df1 = pd.read_csv('csv_files/googletrends-state-raw.csv')
df2 = pd.read_csv('csv_files/googletrends-state.csv')
df3 = pd.read_csv('csv_files/googletrends-state2.csv')

# Since df2 and df3 share year column
merged_df2_df3 = pd.merge(df2, df3, on= ["stname", "year", "fempop1519", "hgabort", "hgpill", "sexft", "virgin", "sexhurt", "hgbc", "index16p", "abort", "bc"], how="inner")
merged_df2_df3.to_csv("csv_files/merged_df2_df3.csv", index="False")

