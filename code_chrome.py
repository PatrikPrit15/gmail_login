from selenium import webdriver  # pip install selenium
import undetected_chromedriver as uc  # pip install undetected_chromedriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


PATH = "C:\Program Files (x86)\chromedriver.exe"  # path k chrome driveru
email = input("zadajte email: ")
heslo = input("zadajte heslo: ")
cas = float(input("zadajte cas medzi krokmi v sekundach: "))

options = Options()
options.add_argument(
    "user-data-dir=D:\\zaloha\\IT\\Projekty\\selenium\\options")
# driver = webdriver.Chrome(chrome_options=options)

driver = uc.Chrome(use_subprocess=True, chrome_options=options)
driver.get("https://mail.google.com/mail/")
time.sleep(cas)

# search=driver.find_element_by_id("Email") #stara verzia
search = driver.find_element(By.ID, "identifierId")  # nova verzia selenia
search.send_keys(email)
time.sleep(cas)


btn = driver.find_element(By.ID, "identifierNext")
btn.click()
time.sleep(cas)

search = driver.find_element(By.NAME, "password")  # nova verzia selenia
search.send_keys(heslo)
time.sleep(cas)

btn = driver.find_element(By.ID, "passwordNext")
btn.click()
time.sleep(cas)


input("enter pre koniec programu")
