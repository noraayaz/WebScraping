import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://editorial.rottentomatoes.com/guide/100-best-classic-movies/'
# db_name = 'Movies.db'
# table_name = 'Top_50'
csv_path = 'C:/Users/Kerem/Desktop/nora_project/PythonProject/top_25_films.csv'
df = pd.DataFrame(columns=["Film","Year", "Header"])

# Get HTML content from the URL
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Find all <h2> tags
headers = data.find_all('h2')

# Initialize an empty DataFrame
df = pd.DataFrame(columns=["Film", "Year", "Header"])

index = 0
while index < 100:
    # Extract film name and year from <h2> tag
    film_name = headers[index].find('a').text
    year = headers[index].find('span').text
    if int(year[1:5]) >= 1950:
    # Construct the data dictionary
        data_dict = {"Film": film_name,
                     "Year": year,
                     "Header": str(headers[index])}  # Storing the entire header HTML content as string
    
    # Create DataFrame for current row
        df1 = pd.DataFrame(data_dict, index=[index])
    
    # Concatenate with main DataFrame
        df = pd.concat([df, df1], ignore_index=True)
    
    index += 1

# Print and save the DataFrame
print(df)
df.to_csv(csv_path, index=False)  # Index is set to False to avoid writing row indices to the CSV file

