from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    # # Do other stuff

# or

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

browser.get(url)
# # do things

browser.close()
