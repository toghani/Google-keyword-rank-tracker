# Google Keyword Ranking Check with Python Script
This script finds the rank of your keywords and automatically imports it in your Google Sheet!
All you have to do is enter the keywords in keywords.txt and the website url in website.txt then run the script, that's it! See the ranking of your words in Google Sheet

## Installation
1. Clone the repository in your local storage (or you can use google colab)
2. Import your keywords in keywords.txt (Each word in a line)
3. Add your website URL in website.txt
4. Enable the API and grab your credentials for [pygsheets](https://github.com/nithinmurali/pygsheets), (Use google sheet in python)
5. Edit 52 and 55 lines in keyword-tracker.py based on the previous step
6. Install robobrowser
```
pip install robobrowser
```
7. Install pygsheets
```
pip install pygsheets
```
8. Enjoy!

### Enable the API for use pygsheets
1.  Head over to the  [Google API Console](https://console.developers.google.com/).
2.  Create a new project by selecting My Project -> + button
3.  Search for 'Google Drive API', enable it.
4.  Head over to 'Credentials' (sidebar), click 'Create Credentials' -> 'Service Account Key'
5.  Select Compute Engine service default, JSON, hit create.
6.  Open up the JSON file, **share your spreadsheet with the "XXX-compute@developer.gserviceaccount.com" email listed.**
7.  Save the JSON file wherever you're hosting your project, you'll need to load it in through Python later.
