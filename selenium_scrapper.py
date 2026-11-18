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

user_textbox = driver.find_element(By.ID, "username")
user_textbox.send_keys(USER)

password_textbox = driver.find_element(By.ID, "password")
password_textbox.send_keys(PASSWORD)

login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

# data-courseid="13855"
# big_data_class_container = driver.find_element(By.ID, "yui_3_18_1_1_1795030350786_27")
course = driver.find_element(By.PARTIAL_LINK_TEXT, "Sistemas de big data")
course.click()

foro_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Práctica")
for foro in foro_link:
    print(foro.text, foro.get_attribute("href"))
    if (
        foro.get_attribute("href")
        == "https://fpadistancia.edu.xunta.gal/mod/forum/view.php?id=2338078"
    ):
        print("Click")
        foro.click()
        break
