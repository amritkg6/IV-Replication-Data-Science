import pandas as pd

df = pd.read_csv('csv_files/merged_df2_df3.csv')

merged_dropped_df2_df3 = df.drop(['index16p', 'stview16pTM', 'stview0809', 'strate16pTM', 'strate0809'], axis=1)
merged_dropped_df2_df3.to_csv('csv_files/merged_dropped_df2_df3.csv', index="False")