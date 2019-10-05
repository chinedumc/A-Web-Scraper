# A-Web-Scraper Built Using BeautifulSoup

This web scraper gets the h-index of Professors of Computer Science listed on the first 25 pages of Google scholar.


## The Rubrics
You can use any scraping library (Selenium or Scrapy or Beautiful Soup and Requests)
Ensure your dataset contains two columns, lecturer’s name and his h-index. 
The lecturer must be a computer science lecturer. This is very important
You should scrape first 25 page results  only.
Note that your submission must be in py format and not ipynb. Also your code must pass 5/10 of pylint tests.

### Getting Started
The first task was to identify use Google Scholar to get Professors of computer science. The search led to the link:
https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=computer+science+professor&btnG=

### Looking Further
1. The task identified from a view of the g-scholar page showed that 10 professors were listed per page.
2. The h-index for each Professor is only obtained on clicking the name of a preofessor which opens a page with more details about the professor such as citations and h-indexes.
3. Each professor had a 'user' tag which is evident on the address bar.


### What To Do
1. With all the necessary programming utilities imported
2. Fetch the name and user tag for each professor from the pages hosting the summarised profiles of each group of 10 professors
3. Then use the tags to open each professor's detailed profile page and fetch the h-index
4. Return the Professor's name and h-index in a csv file.

### Outcome
1. The relevant csv file for 250 Professors of Cmputer Science and their h-indexes was generated and labelled Computer_Science_Professors_and_Their_h-indices.csv
2. The pylint test gave a score above 9.0 

