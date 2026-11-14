import os

# The first line is the indispensable, it imporst the driver among us the web browsesrs
from selenium import webdriver

# This import is for the login
from selenium.webdriver.common.by import By

# The lines after this, are specific for chrome, if we want to scrap another web browswer
# we need to import another modules
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# If we want to use another webbrowser as firefox, we would change chrome to firefox in the imports

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
URL = "https://fpadistancia.edu.xunta.gal/login/index.php"
driver.get(URL)

# Now we are going to do login into the web using selenium
# For this, we need to import By  by common.by
USER = os.environ["FP_USER"]
PASSWORD = os.environ["FP_PASSWORD"]
