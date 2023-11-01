**Hispano review analysis**

The reviews were scrapped from google maps reviews using the chrome extension instant data scrapper to get the csv file.

The columns from that where not useful for the analysis where discarded. The columns that we will be working with are:

- Client
- Time
- review

The time column is in string format indicating how long ago the review was written, to solve this I used regex to get the next format "(number, first letter)" for example for the text "1 seman atras", we will get:

(1,s)