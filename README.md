# Embassy Mailer
---

## Project Info
This project webscrapes emails from a public database of embassies all around the world using Selenium, Chromium and BeautifulSoup. The scraped data is then formatted and listed in a '.csv' format using Pandas, which is then parsed for automatic emailing purposes using smtp servers.

'data.csv' Example:

| Country     | Address         |
|-------------|-----------------|
| Afghanistan | #####@example.com |
| Afghanistan | #####@example.com |
| Afghanistan | #####@example.com |
| Algeria | #####@example.com |
| ...         | #####@example.com |
| Zimbabwe    | #####@example.com |

This is the format which the tool writes the emails and country names to. With the country name being in the first column and the email address being in the second.

---
## Installation
To setup embassy-mailer please make sure you install 'requirements.txt' which can be found in the GitHub repository. This project also uses python3.7 and the Chrome Driver which can be found in Chromium Browser.

### Installing Chrome Driver
Chrome Driver is used for scraping the data from each website and it is necessary to properly get the data needed for the mailer.

#### Linux
```properties
sudo apt install chromium-browser
```
This command should suffice, although you should check to make sure that your chrome driver is found in the directory ```/usr/lib/chromium-browser/chromedriver``` in case any errors are encountered.

Once installation is done I suggest piping the application into a ```log.txt``` file  using ```tee log.txt```.

#### Windows
Please visit https://chromedriver.chromium.org/downloads to find a download for a chrome driver executable. Then change line 38 in ```mailer.py``` to your chrome driver directory.


---
## Common Issues
A common issue encountered with the mailer occurs when signing into your Google account for Gmail. Currently, the best way to get it working is to enable 2FA on your Google account and then to make an app password which you then put into ```mailer.py```. Currently, I have not tested ```mailer.py``` with any other smtp servers.
