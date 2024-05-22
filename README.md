# RottenTomatoes.py
 This Python script is designed to scrape a list of the top 100 classic movies from the Rotten Tomatoes editorial guide. The script focuses on films released in 1950 or later and organizes the data into a structured format.

Technologies Used
*  Python: The primary programming language used.
*  Requests: A Python library utilized to make HTTP requests to retrieve the webpage containing the movie list.
*  Beautiful Soup: Employed for parsing HTML and extracting data, enabling the isolation of specific content within web pages.
*  Pandas: A powerful data manipulation library used to create and handle the DataFrame containing the movie details.

Functionality
*  Data Extraction: The script fetches the HTML content of the specified URL and uses Beautiful Soup to parse it, extracting movie names, release years, and their corresponding HTML headers.
*  Data Filtering: It filters the movies to include only those released from 1950 onwards.
*  Data Storage: The data is stored in a DataFrame with columns for the film's name, year, and the full HTML content of the h2 tag, which includes additional descriptive text about the film.
*  File Output: The DataFrame is then saved to a CSV file on the user's desktop, providing a convenient way to access or analyze the scraped data offline.

  # WebScraping.py
 This Python script is designed to scrape a list of the top 50 highly-ranked films from a webpage archived on the Wayback Machine. It extracts specific data about these films and stores it in both a CSV file and a SQLite database.

Technologies Used
* Python: The main programming language used in the script.
* Requests: Utilized to fetch the HTML content of the webpage.
* Beautiful Soup: Used for parsing HTML and extracting necessary data, such as film names, average rankings, and release years.
* Pandas: Employs this library to handle data frames and facilitate data manipulation.
* SQLite3: Enables database operations, storing the data in a structured and queryable format.
  
Functionality

* Data Extraction: Retrieves the HTML page, parses it using Beautiful Soup, and navigates through the table of films to extract data.
* Data Storage:
  * CSV Output: Stores the top 50 films' data into a CSV file named top_50_films.csv for easy offline access and analysis.
  * Database Storage: [Currently commented out] Designed to save the data into a SQLite database named Movies.db, which can be utilized for more complex queries and persistent storage.
* Filtering and Loop Control: Limits the extraction to the first 50 entries to conform to the project's scope of 'Top 50 films'.
  
Purpose

The script is developed to provide film enthusiasts, researchers, or data analysts with structured access to information on highly-ranked films. By facilitating easy access to this data through both a CSV file and a relational database, the script supports various forms of data analysis and visualization.


