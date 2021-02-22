import os
import requests
from urllib import request
import subprocess
import asyncio
from selenium import webdriver
import time
# os.system("open /Applications/Google Chrome.app")
#
# subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Google Chrome.app"])

driver = webdriver.Chrome()
driver.get("https://bugly.qq.com/v2/crash-reporting/dashboard/4a44bfe394?pid=2")

if driver.current_url != "https://bugly.qq.com/v2/crash-reporting/dashboard/4a44bfe394?pid=2":
    time.sleep(10)
    driver.find_element_by_css_selector("#qlogin_list > a").click()



