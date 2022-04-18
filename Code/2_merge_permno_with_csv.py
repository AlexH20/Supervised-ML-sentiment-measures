import pandas as pd
import os

#Use txt file with tickers to upload on wrds to get permnos as csv (select only latest permnos):https://wrds-www.wharton.upenn.edu/pages/get-data/center-research-security-prices-crsp/annual-update/tools/translate-to-permcopermno/

input_file_path = "INPUT FILE PATH"
permnocsv_path = "PERMNO FILE PATH"
output_file_path = "OUTPUT FILE PATH"

# read csv data and adjust columns from csv file output from wrds
df1 = pd.read_csv(input_file_path)
df2 = pd.read_csv(permnocsv_path)
df2.columns = ["Date", "Ticker", "Text"]

#Merge both csv files based on Ticker
data = df1.merge(df2,
                      on ="Ticker",
                      how = "left")

#Change column names since merging produces weird column names
data.columns = ['Date', 'Ticker', 'Text', 'Date_Permno', 'Permno']

#Delete the permno release date
del data["Date_Permno"]

#Drop observations where wrds database hasn't found any permno code
data.dropna(inplace = True)

#Write file to csv for further use
os.remove(input_file_path)
data.to_csv(output_file_path + "data_processed.csv", sep = "," )


