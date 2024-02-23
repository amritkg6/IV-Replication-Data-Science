import pandas as pd

# Load your main dataset
dataset = pd.read_csv('csv_files/merged_dropped_df2_df3.csv')

# Load the Twitter data
twitter_data = pd.read_csv('csv_files/twitter.csv')


print(dataset.columns)
print(twitter_data.columns)


# Example of renaming columns in the twitter_data DataFrame
twitter_data.rename(columns={
    'Log Tweet Rate: Birth Control': 'birth_control_tweet_rate',
    'Log Tweet Rate: Abortion': 'abortion_tweet_rate'
    # Add more mappings here if you have more columns
}, inplace=True)

# Rename the 'abort' column in your main dataset to match the naming convention
dataset.rename(columns={
    'abort': 'abortion_rate'
    # Add any other column renames here
}, inplace=True)
# Convert to string if these are categorical or identifier variables
dataset['abortion_rate'] = dataset['abortion_rate'].astype(str)
twitter_data['abortion_tweet_rate'] = twitter_data['abortion_tweet_rate'].astype(str)
# Merging datasets on a common column, e.g., 'date'
merged_dataset = pd.merge(dataset, twitter_data, left_on='abortion_rate', right_on='abortion_tweet_rate', how='left')

print(merged_dataset.head())
