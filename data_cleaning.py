import os
import numpy as np
import pandas as pd

print("--- [STEP 2] DATA CLEANING PIPELINE STARTED ---\n")

# 1. Raw Data ko Load Karna
# Agar aapne file bina folder ke direct bahaar rakhi hai, toh hum seedhe naam se load karenge
try:
    df = pd.read_csv("raw_customer_churn.csv")
except FileNotFoundError:
    file_path = os.path.join("Raw_Data", "raw_customer_churn.csv")
    df = pd.read_csv(file_path)

print(f"📊 Initial Data Loaded: {df.shape[0]} Rows, {df.shape[1]} Columns\n")

# 2. Duplicates Hatana
df_clean = df.drop_duplicates().reset_index(drop=True)
print(f"🔄 2.1: Duplicates Removed. Rows {df.shape[0]} se kam hokar {df_clean.shape[0]} ho gayi hain.")

# 3. TotalCharges Column Ko Text Se Number (Float) Mein Badalna
df_clean['TotalCharges'] = df_clean['TotalCharges'].astype(str).str.replace('$', '', regex=False)
df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce') 
print("🔤 2.2: 'TotalCharges' column se garbage text saaf karke use float numeric type banaya.")

# 4. Outliers Handle Karna
age_median = df_clean['Age'].median()
df_clean.loc[(df_clean['Age'] < 18) | (df_clean['Age'] > 100), 'Age'] = age_median

charges_median = df_clean['MonthlyCharges'].median()
df_clean.loc[df_clean['MonthlyCharges'] > 200, 'MonthlyCharges'] = charges_median
print("🚨 2.3: Age aur MonthlyCharges ke extreme outliers ko fix kiya.")

# 5. Missing Values (NaN) Imputation
total_charges_mean = np.round(df_clean['TotalCharges'].mean(), 2)
df_clean['Age'].fillna(age_median, inplace=True)
df_clean['TotalCharges'].fillna(total_charges_mean, inplace=True)
df_clean['Gender'].fillna('Unknown', inplace=True)
print("📊 2.4: Missing Values successfully fill ho gayi hain.")

# 6. Cleaned Data Ko Save Karna
df_clean.to_csv("cleaned_customer_churn.csv", index=False)
print(f"\n✅ [SUCCESS] Cleaned data saved as 'cleaned_customer_churn.csv'")
print(df_clean.info())

import pandas as pd