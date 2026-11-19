import getpass
from time import sleep

import selenium.webdriver.support.expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox(service=Service("/snap/bin/geckodriver"))

url_foro = "https://fpadistancia.edu.xunta.gal/mod/forum/view.php?id=2338078"

username = "ue567618"
password = getpass.getpass("Password:")

driver.get(url_foro)
threads = {}

user_textbox = driver.find_element(By.ID, "username")
user_textbox.send_keys(username)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)

login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

sleep(2)

while True:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".table.discussion-list.generaltable")
        )
    )
    page_html = driver.page_source
    soup = BeautifulSoup(page_html, "html.parser")
    forum_table = soup.find("table", class_="table discussion-list generaltable")
    discussions = forum_table.find_all("tr", class_="discussion")

    for discussion in discussions:
        author = (
            discussion.find("td", class_="author")
            .find("div", class_="text-truncate")
            .text.strip()
        )
        title = discussion.find("th").find("a").text.strip()
        last_comment_author = (
            discussion.find("td", class_="text-start")
            .find("div", class_="text-truncate")
            .text.strip()
        )
        comment_count = (
            discussion.find(
                "td", class_="p-0 text-center align-middle fit-content px-2"
            )
            .find("span")
            .text.strip()
        )

        thread_id = discussion.get("data-discussionid")

        if thread_id not in threads:
            threads[thread_id] = {
                "title": title,
                "author": author,
                "last_comment_author": last_comment_author,
                "comment_count": comment_count,
            }
            print(f"Nuevo hilo titulado {title} de {author}")

        if threads[thread_id]["comment_count"] != comment_count:
            print(
                f"{last_comment_author} ha publicado una nueva respuesta (la {comment_count}) al hilo {title}"
            )
            threads[thread_id]["comment_count"] = comment_count
            threads[thread_id]["last_comment_author"] = last_comment_author

    sleep(5)
    driver.refresh()
