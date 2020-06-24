This directory contains the code associated with collecting Google Alerts data. It contains -

1. `get_mails.gs`: A Google Script file used to convert all the Google alert mails to pdf and download in the local storage. Also contains the key words Alerts were set up for.

2. `get_urls_by_scraping_mail_pdfs.py`: From the collected pdfs, scrape to list all URLs of the articles Google Articles suggested. Outputs an `output.csv` containg the list.

3. `Download And Store.ipynb`: Downloads articles from the URLs, identifies events, validates prediction (manual), and finally outputs a pickle file.