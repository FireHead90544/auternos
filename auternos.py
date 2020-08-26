from selenium import webdriver
import time
import sys
import os

driver = webdriver.Chrome('/path/to/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/path/to/bin/chromium"
driver = webdriver.Chrome(options=options)
driver.get('https://aternos.org/servers/')

# log in
text_area = driver.find_element_by_id('user')
text_area.send_keys("username")

text_area = driver.find_element_by_id('password')
text_area.send_keys("password")

login = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div[3]/div[4]')
login.click()

time.sleep(3)

# select server
select = driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]')
select.click()

# wait for the page to load
time.sleep(5)

# click start button
start = driver.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div[4]/div[1]')
start.click()

time.sleep(5)

# click cancel
cancel = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/main/div/a[2]')
cancel.click()

time.sleep(3)

#close chromium and python
os.system("killall chromium")
sys.exit()
