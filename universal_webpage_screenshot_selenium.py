from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# requirements - 
# pip install selenium

# change these fields - url, filename, width (defaulted to 1366)

url = 'https://www.google.com'
option = Options()
option.add_argument('-headless')
browser = webdriver.Firefox(options=option)

browser.get(url)

width = 1366
height = browser.execute_script('return document.body.parentNode.scrollHeight')
# for firefox add 74 to the height returned
browser.set_window_size(width, height + 74)

element = browser.find_element_by_tag_name('body')
element.screenshot(filename)

browser.quit()

