# Real Estate Dash: Overview  
* Built a web scraper for Redfin using Python and Selenium and obtained details from listings in specified locations (for recent 3 months)  
* Intentionally let scraper obtain messy data to require cleaning  
* Used Python (Pandas) to transform the scraped data into a usable format  
* Created a dashboard using Plotly Dash and integrated into a web app using Django  

## Requirements  
**Python Version:** 3.6.12  
**Packages:** Plotly Dash (vTBD), Django (v3.1.5), gunicorn (v20.0.4), whitenoise (v5.2.0)  
**Deploying Django app on Heroku with Docker:** https://testdriven.io/blog/deploying-django-to-heroku-with-docker/
**Custom Domain w/ Heroku:** https://devcenter.heroku.com/articles/custom-domains  
**HTML/CSS Template:** https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_startup  

## Web Scraping  
Scrapes the following details from the listing pages:  
* Address info: street, city, state, zip_code  
* Home info: price, beds, baths, sqft, home_type, sold_history  
* Neighborhood info: neighborhood, walk_score, transit_score, bike_score  

## Dashboard
Purpose of dashboard
