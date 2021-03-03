import pandas as pd

pd.set_option('display.width', 2000)
pd.set_option('display.max_columns', 20)

# Importing of the data set
df = pd.read_csv('salesdaily.csv')

# Data Quality and Structure
df.info()

# M01AB — Anti-inflammatory and antirheumatic products, non-steroids, Acetic acid derivatives and related substances
# M01AE — Anti-inflammatory and antirheumatic products, non-steroids, Propionic acid derivatives
# N02BA — Other analgesics and antipyretics, Salicylic acid and derivatives
# N02BE — Other analgesics and antipyretics, Pyrazolones and Anilides
# N05B — Psycholeptics drugs, Anxiolytic drugs
# N05C — Psycholeptics drugs, Hypnotics and sedatives drugs
# R03 — Drugs for obstructive airway diseases
# R06 — Antihistamines for systemic use

# Taking a peek at data
print(df.head())

print(df.describe())

# change for niv