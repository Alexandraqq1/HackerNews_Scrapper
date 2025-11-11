import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape_hackernews():
    # pornesc broswerul chrome cu selenium
    print("Se porneste browserul")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # deschid hackernews
    driver.get("https://news.ycombinator.com/")
    time.sleep(5)

    print("Se colecteaza datele")

    # caut toate elementele HTML care reprezinta o stire
    items = driver.find_elements(By.CSS_SELECTOR, ".athing")

    # creez o lista in care audaug fiecare stire
    data = []


    # creez un loop care navigheaza printre toate elementele de tip stire
    for item in items:
        # titlul
        title_elem = item.find_element(By.CSS_SELECTOR, ".titleline a")
        # textul din titlu
        title = title_elem.text
        # linkul catre stire
        link = title_elem.get_attribute("href")

        # (tr / td -> autorul si scorul )
        try:
            subtext = item.find_element(By.XPATH, "following-sibling::tr[1]//td[@class='subtext']")
            score = subtext.find_element(By.CLASS_NAME, "score").text  # ex: "123 points"
            author = subtext.find_element(By.CLASS_NAME, "hnuser").text  # numele autorului
        except:
            score = "N/A"
            author = "N/A"

        # Adaug toate datele intr un dictionar
        data.append({
            "Titlu" : title,
            "Autor" : author,
            "Scor" : score,
            "Link" : link,
            "Data" : pd.Timestamp.now() # data la care am extras sitrea
        })

    # inchidem browserul
    driver.quit()

    print("Date extrase", len(data))

    # transformam totul in DataFrame
    return pd.DataFrame(data)