from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

options = Options()
options.binary_location = r"C:/Users/Adilkhan/.cache/selenium/firefox/win64/125.0.3/firefox.exe"

fp = webdriver.FirefoxProfile('C:/Users/Adilkhan/AppData/Local/Temp/rust_mozprofile52nj5M')
driver = webdriver.Firefox(firefox_profile=fp, options=options, executable_path="C:/Program Files/geckodriver.exe")
wait = WebDriverWait(driver, 20)

driver.get("https://web.whatsapp.com/")
driver.maximize_window()

try:
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[title="𝟰𝗿𝗮𝗯𝗲𝘁 𝗟𝗼𝗴𝗼 𝗣𝗿𝗼𝗺𝗼𝘁𝗶𝗼𝗻 "]')))
    element.click()
    print("Element clicked successfully!")
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')))
    element.click()
    print("Element clicked successfully!")
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[5]/span/div/span/div/div/div/section/div[6]/div[2]/div[3]/div[2]/div/span/div')))
    element.click()
    print("Element clicked successfully!")
except Exception as e:
    print("Error:", str(e))


seen_data = set()


def scroll_and_parse(element_xpath):
    increment = 504
    scrollable_element = driver.find_element(By.XPATH, element_xpath)
    last_height = driver.execute_script("return arguments[0].scrollTop", scrollable_element)

    while True:
        driver.execute_script(f"arguments[0].scrollTop += {increment}", scrollable_element)
        time.sleep(0.5)

        containers = driver.find_elements(By.CLASS_NAME, "_ak8q")
        containers_2 = driver.find_elements(By.CLASS_NAME, "_ajzr")

        for container in containers_2:
            text = container.text
            if text not in seen_data:
                print(text)
                seen_data.add(text)

        for container in containers:
            text = container.text
            if text not in seen_data:
                print(text)
                seen_data.add(text)

        new_height = driver.execute_script("return arguments[0].scrollTop", scrollable_element)
        if new_height == last_height:
            break
        last_height = new_height

        save_data_to_file(seen_data)

def save_data_to_file(data_set):
    with open('output.txt', 'w', encoding='utf-8') as file:
        for data in data_set:
            file.write(f"{data}\n")

scroll_and_parse('/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div/div[2]')

driver.quit()


