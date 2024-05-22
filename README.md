# WebScraping
   RottenTomatoes.py(bold)
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
