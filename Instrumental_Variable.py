import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.sandbox.regression.gmm import IV2SLS

# Load the dataset
df = pd.read_csv('csv_files/merge_datasets.csv')  # Adjust with your actual dataset path

# Data Cleaning Steps
df.replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace infinite values with NaN

# Example: Fill NaN values for 'sexft' and 'birth control: (United States)' with the mean or median
df['sexft'].fillna(df['sexft'].mean(), inplace=True)
df['birth control: (United States)'].fillna(df['birth control: (United States)'].median(), inplace=True)
df['16 and pregnant: (United States)'].fillna(df['16 and pregnant: (United States)'].mean(), inplace=True)

# Continue with your analysis only if df is not empty
if not df.empty:
    # Define variables
    Y = df['abort']
    X = df[['sexft', 'birth control: (United States)']]
    X = sm.add_constant(X)
    Z = df['16 and pregnant: (United States)']

    # Perform IV Estimation
    iv_model = IV2SLS(Y, X, Z).fit()

    # Print the summary of the IV estimation
    print(iv_model.summary())
else:
    print("DataFrame is empty after handling missing values.")

# Assuming 'iv_model' is your IV2SLS model result
summary = iv_model.summary().as_text()

# Specify the path and filename for your results
results_path = 'iv_results.txt'

# Save the summary to a file
with open(results_path, 'w') as f:
    f.write(summary)
