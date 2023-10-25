from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://jpdb.io/kanji-by-frequency"

def scrape_kanji(browser):
    # Open the target URL
    browser.get(URL)

    # Ensure that the content has been loaded
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr td div a"))
    )
    time.sleep(2)  # Extra wait to make sure all dynamic content is loaded

    # Extract kanji
    kanji_elements = browser.find_elements(By.CSS_SELECTOR, "table tbody tr td div a")
    kanji_list = [el.text for el in kanji_elements]

    return ''.join(kanji_list)


if __name__ == "__main__":
    # Setup the driver. You might need to specify the path if the driver isn't in your PATH
    browser = webdriver.Chrome()

    kanji_string = scrape_kanji(browser)
    
    with open("kanji_by_frequency.txt", "w", encoding="utf-8") as f:
        f.write(kanji_string)

    browser.quit()
    print("Kanji scraped and saved to kanji_by_frequency.txt")
