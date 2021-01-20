# Real Estate Dash: Overview  
* Built a web scraper for Redfin using Python and Selenium and obtained details from listings in specified locations (for recent 3 months)  
* Intentionally let scraper obtain messy data to require cleaning  
* Used Python (Pandas) to transform the scraped data into a usable format  
* Created a dashboard using Plotly Dash and integrated into a web app using Flask  

## Requirements  
**Python Version:** 3.8.5  
**Packages:** Flask (v1.1.2), gunicorn (v20.0.4), Plotly Dash (TBD)  
**Deploying Flask app on Heroku:** https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true  

## Web Scraping  
Scrapes the following details from the listing pages:  
* Address info: street, city, state, zip_code  
* Home info: price, beds, baths, sqft, home_type, sold_history  
* Neighborhood info: neighborhood, walk_score, transit_score, bike_score  

## Dashboard
Purpose of dashboard
