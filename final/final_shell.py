from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
# ----------------------------------------
# 1) start your virtual environment :
# mac: source .venv/bin/activate
# windows: .\venv\Scripts\activate ??
# 2) pip install webdriver_manager
# 3) pip install selenium
# ----------------------------------------
driver = webdriver.Chrome() # the driver is what opens the applications and runs through the following code on the website
driver.implicitly_wait(10)
url = "https://quotes.toscrape.com/"
driver.get(url)

# --------------YOUR CODE GOES HERE -------------- 
# There are four tasks worth 10 pts each (if you haven't finished the entire project, you can still get partial credit)
# TODO: Print out the first quote by Einstein (10 pts)
# hint: you can extract the text by using .textContent on the element


# TODO: Print out the top ten tags (10 pts)
# hint: you want to find the div that contains the top ten tags, then use a for loop to print them out


# TODO: Click the login button (10 pts)
# hint: click it the same way we clicked the google search button


# TODO: Login (you can use any username and password) (10 pts)
# hint: to enter text, use the send_keys() function that we used in web-scraping-shell.py (the web scraping practice)


# ------------------------------------------------

time.sleep(15)
driver.close()
