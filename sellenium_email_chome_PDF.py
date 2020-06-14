from selenium import webdriver
#1.import the driver library from selenium#
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import pyautogui
import json
#driver= webdriver.Chrome("C:\\Users\\wtsje\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\chromedriver_win32\\chromedriver.exe")
#2.import the PATH/location of the driver software#

#driver.get("https://www.haveibeenpwned.com")


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.get("https://www.haveibeenpwned.com")

edit_txt_email = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='Account']"))).send_keys("ohgheeling80@gmail.com") 
prs_btn = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='searchPwnage']"))).click() 
com_acc = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'paste accounts')]"))).click()                                                                                                       
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}
sleep(6)
options.add_experimental_option('prefs', profile)
options.add_argument('--kiosk-printing')
driver.execute_script('window.print();')
driver.quit()
