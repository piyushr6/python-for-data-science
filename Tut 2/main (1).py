import numpy as np
import pandas as pd
from scipy.stats import trim_mean

df = pd.read_csv('python-for-data-science/data.csv')

mean_value = df['Values'].mean()
median_value = df['Values'].median()
variance_value = df['Values'].var()
std_dev_value = df['Values'].std()

trimmed_mean_value = trim_mean(df['Values'], proportiontocut=0.1)

percentiles = df['Values'].quantile([0.1, 0.25, 0.5, 0.75, 0.9])
iqr_value = percentiles[0.75] - percentiles[0.25]

lower_mild_threshold = percentiles[0.25] - 1.5 * iqr_value
upper_mild_threshold = percentiles[0.75] + 1.5 * iqr_value
lower_extreme_threshold = percentiles[0.25] - 3 * iqr_value
upper_extreme_threshold = percentiles[0.75] + 3 * iqr_value

mild_outliers = df[(df['Values'] < lower_mild_threshold) | (df['Values'] > upper_mild_threshold)]
extreme_outliers = df[(df['Values'] < lower_extreme_threshold) | (df['Values'] > upper_extreme_threshold)]
print(f"Average: {mean_value}")
print(f"Middle Value: {median_value}")
print(f"Dispersion: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
print(f"10% Truncated Mean: {trimmed_mean_value}")
print(f"10th Percentile: {percentiles[0.1]}")
print(f"25th Percentile (First Quartile/Q1): {percentiles[0.25]}")
print(f"50th Percentile (Second Quartile/Median/Q2): {percentiles[0.5]}")
print(f"75th Percentile (Third Quartile/Q3): {percentiles[0.75]}")
print(f"90th Percentile: {percentiles[0.9]}")
print(f"Interquartile Range (IQR): {iqr_value}")
print(f"Moderate Outliers: {mild_outliers}")
print(f"Severe Outliers: {extreme_outliers}")