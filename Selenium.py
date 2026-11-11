#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

import time
import os
from os.path import exists
import shutil

# The following 3 lines are for ubuntu only. If windows, please comments then to work well..
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()

downloadDir = os.path.abspath(".") + os.sep

preferences = {
    "download.default_directory": downloadDir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", preferences)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--window-size=1200,1200")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
try:
    driver.execute_cdp_cmd("Page.setDownloadBehavior", {
        "behavior": "allow",
        "downloadPath": downloadDir
    })
except Exception as e:
    print(f"CDP setDownloadBehavior warning: {e}")

def wait_for_download(before_set, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        time.sleep(1)
        after_set = set(os.listdir(downloadDir))
        new_files = [f for f in (after_set - before_set) if not f.endswith('.crdownload') and not f.endswith('.tmp')]
        if new_files:
            return new_files[0]
    # Fallback to newest csv
    csvs = [f for f in os.listdir(downloadDir) if f.endswith('.csv')]
    if csvs:
        csvs.sort(key=lambda x: os.path.getmtime(os.path.join(downloadDir, x)), reverse=True)
        return csvs[0]
    return "auction.csv"

before_files = set(os.listdir(downloadDir))
driver.get('https://www.twse.com.tw/zh/announcement/auction.html')
time.sleep(2)
element = driver.find_element(by=By.CLASS_NAME, value="csv")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
time.sleep(1)
driver.execute_script("arguments[0].click();", element)

DownloadedFilename = wait_for_download(before_files)
print(f"DownloadedFilename: {DownloadedFilename}")

if DownloadedFilename and DownloadedFilename != "auction.csv":
    shutil.copy(DownloadedFilename, "auction.csv")
    print(f"File '{DownloadedFilename}' copied to 'auction.csv'.")
    if os.path.exists(DownloadedFilename) and DownloadedFilename != "auction.csv":
        try:
            os.remove(DownloadedFilename)
        except Exception:
            pass

print("Download completed...", os.path.join(downloadDir, 'auction.csv'))
driver.quit()
