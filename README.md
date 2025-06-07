# Luftwerte Shanghai to Airtable

This repository contains a simple script to fetch the Air Quality Index (AQI)
for Shanghai and store it in an Airtable base. The script can be scheduled to
run daily (e.g. via cron) and uses the WAQI API and Airtable's REST API.

## Requirements
- Python 3 with the `requests` library
- Environment variables for API access:
  - `WAQI_TOKEN`: token for the World Air Quality Index API
  - `AIRTABLE_API_KEY`: your Airtable API key
  - `AIRTABLE_BASE_ID`: the ID of your Airtable base
  - `AIRTABLE_TABLE_NAME`: the table where records should be created

## Usage
```
python fetch_airquality_to_airtable.py
```
Ensure all required environment variables are set before running.

To run the script every morning, create a cron job like the following:
```
0 8 * * * /usr/bin/python3 /path/to/fetch_airquality_to_airtable.py >> /var/log/aqi.log 2>&1
```
This example runs the script at 8 AM every day.
